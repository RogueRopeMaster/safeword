---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality and strong art direction. Use when asked to build or redesign web components, pages, dashboards, landing pages, or full web apps in HTML/CSS/JS or frontend frameworks, especially when originality, visual polish, and interaction design are important.
license: Complete terms in LICENSE.txt
---

# Frontend Design

Create real frontend code with a distinctive visual identity, not generic template styling.

## Workflow

1. Clarify the product context.
- Identify purpose, audience, technical stack, and constraints (performance, accessibility, browser support, design system requirements).

2. Commit to one bold design direction.
- Choose a strong point-of-view before coding (for example: editorial, brutalist, art deco, playful toy-like, industrial utility, maximalist collage, refined luxury, retro-futuristic).
- State one memorable differentiator that the design will emphasize.

3. Translate direction into a visual system.
- Define CSS variables for colors, spacing, radius, shadows, and motion timing.
- Choose expressive typography with intentional pairing (display + body).
- Define layout logic (grids, asymmetry, overlap, density, negative space).

4. Build production-grade UI.
- Implement working code in the requested stack (HTML/CSS/JS, React, Vue, etc.).
- Ensure responsive behavior on mobile and desktop.
- Create meaningful states (hover, focus, active, loading, disabled, empty).

5. Add purposeful motion.
- Prioritize a small number of high-impact animations: entry sequence, staggered reveals, scroll-triggered moments, and intentional hover transitions.
- Keep motion coherent with the design direction and content hierarchy.

6. Perform quality checks.
- Verify accessibility basics: semantic structure, keyboard navigation, visible focus states, contrast, reduced-motion support.
- Verify runtime quality: no broken interactions, no placeholder-only markup, no dead code.

## Design Standards

- Commit to intentional typography.
- Avoid generic defaults such as Inter, Roboto, Arial, and unconsidered system stacks unless the existing project design system explicitly requires them.
- Pair typefaces with contrast in personality and function.

- Commit to a strong color strategy.
- Use a dominant palette with controlled accent colors.
- Avoid timid, evenly distributed palettes and avoid overused purple-gradient-on-white patterns.

- Commit to spatial character.
- Prefer layouts with deliberate rhythm, asymmetry, and hierarchy over cookie-cutter component grids.
- Use overlap, framing devices, section breaks, or grid-breaking elements when aligned with the concept.

- Commit to atmospheric backgrounds and details.
- Use gradients, textures, patterns, shapes, overlays, or depth effects to build context.
- Avoid flat, context-free backgrounds unless minimalism is an explicit design choice.

- Commit to differentiated interaction design.
- Build interactions that feel authored for this product, not generic UI kit defaults.

## Guardrails

- Never output fake design language without working implementation.
- Never deliver visually generic, interchangeable "AI slop" layouts.
- Never ignore existing product design constraints when working inside an established codebase.
- Preserve established patterns when the task explicitly targets an existing design system.

## Output Requirements

- Provide complete, runnable code for the requested scope.
- Keep code organized and maintainable.
- Explain key design and implementation decisions briefly.
- Include any required setup steps only when needed by the stack.
