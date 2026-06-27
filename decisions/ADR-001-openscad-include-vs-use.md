# ADR-001: OpenSCAD `include` vs `use` + `$fn` Convention

**Status:** Accepted

## Context

Every OpenSCAD project must decide how files reference each other. OpenSCAD provides two mechanisms with fundamentally different semantics:

- **`include <file.scad>`** — executes the referenced file in the current scope. Variables, constants, and any top-level geometry in the included file all become part of the including file's scope. This is the only way to share global variables (dimension constants, color values) across files.
- **`use <file.scad>`** — imports only module and function definitions. Top-level geometry in the used file does *not* execute. Critically: **variables are NOT exported**. Any global variable defined in the used file is invisible to the caller.

The failure mode for the wrong choice is silent: calling `use <params.scad>` causes every dimension constant (`ROOM_W`, `DESK_H`, `COLOR_CREAM`, etc.) to resolve to `undef`. OpenSCAD does not error on `undef` — it silently produces zero-dimension or degenerate geometry. The model appears to render; the output is wrong.

This project's architecture centres on a single `params.scad` file that is the source of truth for all dimension constants and brand color values. Correct propagation of those constants to every consuming file is a correctness requirement, not a style preference.

A second issue: `$fn` (the facet-count resolution for curved geometry) is a global variable. Setting it high globally during development causes exponential render-time growth as the room model grows. A room model with 15+ furniture items at `$fn=64` can take 20+ minutes to render under CGAL; at `$fn=12` the same model renders in seconds. The Manifold backend (available in the `openscad@snapshot` dev release) mitigates this somewhat, but the convention must be set before the model grows.

## Decision

1. **`params.scad` is always loaded with `include`**, never `use`:
   ```openscad
   include <../../params.scad>   // correct — variables exported
   // use <../../params.scad>    // wrong — variables silently undef
   ```

2. **Furniture, zone, and accessory module files are loaded with `use`** from the files that compose them. This imports only the module definitions (`standing_desk()`, `focus_desk_zone()`, etc.) without executing any top-level geometry at the origin:
   ```openscad
   use <../furniture/standing-desk.scad>   // module definition only
   use <../furniture/shelving.scad>
   ```

3. **`$fn` is set to `~12` during development** (interactive preview and development renders). It is raised to `64` only for committed render artifacts and STL exports — and only at the top level of the view file, never inside reusable modules.

The mnemonic: **`include` for data, `use` for modules.**

## Consequences

**What becomes easier:**

- Every `.scad` file that begins with `include <../../params.scad>` has guaranteed access to all dimension and color constants. There is no silent `undef` failure mode.
- Using `use` for module files prevents "ghost geometry" — furniture modules do not inadvertently draw themselves at the origin when included by a zone file.
- Development iteration is fast: `$fn=12` previews run in seconds even as the room model grows to 20+ furniture and accessory items.
- The OpenSCAD rule is clearly documentable and enforceable in code review: any file using `use <params.scad>` is immediately wrong.

**What becomes harder or requires attention:**

- The `include` of `params.scad` means all top-level variable assignments execute in the including file's scope. Any local variable that shadows a `params.scad` name will silently override it. Prevention: `params.scad` uses `UPPER_SNAKE_CASE` for all names; local variables in model files use `lower_case`. This naming convention is a direct consequence of the `include` choice.
- Files that `include` a file that itself contains `include` calls can create deeply nested include chains. Keep `params.scad` leaf-level: it must not itself `include` any other file.
- Final STL and committed render artifacts require a deliberate `$fn` raise step (or a Makefile variable override) to produce smooth curves. This is a workflow step, not a one-time setup. The Makefile must document the override pattern.
