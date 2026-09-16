# FIX-08 inquiry feedback

Production starting point verified September 16: `73e62571742ac46c63e9626bc5e87ce0336aa345`, deployment `dpl_FcY8f3jqzEWYTtGS6rpZWuMLFotb`, project `prj_AYu4RUfH5DbpHXj4eSINVGaYnH8p`, domain underwriter.fusiondataco.com. Commercial target isolated from client instances.

Reproduced with current production HTML/JS in a fresh 390x844 browser and intercepted fictional API/auth responses: submission succeeded but global `Request completed.` status was at y=-750, outside viewport, and no stable inquiry ID was visible. No production inquiry or provider request was created.

Repair places pending/success/error status beside Submit inquiry, announces errors, reports a stable server-returned request ID, and scrolls feedback into view. Success survives a subsequent list-refresh failure with explicit instructions not to resubmit. Lost-response retries reuse the original ID; failed requests preserve fields. JSON validation includes per-field errors and focuses invalid inputs. Unexpected HTML produces human-readable retry feedback. Existing database persistence and ownership queries remain unchanged.

Checks: npm run build passes JavaScript/Python syntax. Browser fixture test `PLAYWRIGHT_PACKAGE=/path/to/package.json node scripts/test-inquiry-browser.mjs` passes success/reload, lost-response retry with one fixture record, post-save refresh failure, field validation, and HTML service error. Playwright may be installed in this project or provided through PLAYWRIGHT_PACKAGE pointing to an existing package.json whose dependencies include it. These fixtures prove UI/network behavior, not live database persistence.

Remaining: isolated authenticated production inquiry and operator queue visibility; real tenant isolation and no-spend durable database retry acceptance. Do not mark FIX-08 complete until those pass. No paid purchases, emails, customer writes or environment-file reads occurred.
