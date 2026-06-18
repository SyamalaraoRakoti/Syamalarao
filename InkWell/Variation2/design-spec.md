# Design Specification: Inkwell Rewritten
**Author:** Søren (WebGL Experience Designer)

## 1. Concept: The Infinite Library
As we address the **29.1% decline in footfall** over the last two years, our landing page must be more than a form—it must be an experience that re-establishes Inkwell as a destination. The "Infinite Library" concept uses WebGL to create an immersive, candle-lit space that mirrors the "third place" feeling our customers crave.

## 2. Experience Wireframe
1. **Hero (The Bloom):** A single drop of ink falls and blossoms into the Inkwell logo. Headline: *"Inkwell, rewritten."* CTA: *Claim your Library Card*.
2. **The Drift (Storytelling):** Camera glides through a 3D space of floating shelves. Pinned text: *Rediscover the third place.*
3. **The Proof (Value):** Reveal three cards detailing what they unlock:
   - A free book.
   - Members-only author events.
   - A digital card for your phone.
4. **The Sign-Up (The Ex-Libris):** The final scene features a gold-foil *ex-libris* bookplate (our Library Card). The email form appears here.

## 3. Technical Choreography
- **Camera:** Scroll-progress mapped to camera Z-position. Uses `damp` for smooth movement.
- **Visuals:** `InstancedMesh` for books (low draw calls), GPU particles for floating pages. Post-processing bloom for candle-light.
- **Primary CTA:** The *ex-libris* card itself. On hover, it glows slightly (`#C9A227`). On success, the card flips to display "Member since 2026."

## 4. Accessibility & Fallbacks
- **`prefers-reduced-motion`:** If enabled, the page renders a static hero with the ink-bloom logo and a standard scrolling layout.
- **No-WebGL Fallback:** If the browser fails to render, we fall back to a beautifully typeset static hero (`#F4ECD8` background, `#0B0F1A` text) and a clean, high-contrast form.
- **Accessibility (A11y):** All text is in the DOM for screen readers. The `<canvas>` is `aria-hidden`. The form has explicit `<label>` elements and visible focus rings that satisfy AA contrast standards.

## 5. Success Metric
The success of this design is measured by the conversion of anonymous visitors into identified "Library Card" holders, directly impacting the **€31,695 potential monthly revenue uplift** identified in our diagnosis.
