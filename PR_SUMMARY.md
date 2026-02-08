# Pull Request Summary

## Title

Fix dead links in Strategic Communication category (Feb 2026)

## Description

This PR removes 4 dead initiatives and updates 1 URL in the Strategic Communication (הסברה) category based on automated testing and manual verification conducted on February 7, 2026.

## Changes Made

### Removed Initiatives (Dead DNS/Domains):

1. **BlueWhitePublicity** (הסברה כחול לבן)
   - URL: https://www.hasbaracahollavan.com/
   - Status: DNS not resolving
   - Location: Main/links.json

2. **israelfightsback** (ישראל נלחמת בחזרה)
   - URL: http://israelfightsback.info/
   - Status: DNS not resolving
   - Location: SocialNetworks/links.json

3. **ShareItIl** (שייר איט ישראל)
   - URL: https://shareitil.com/
   - Status: DNS not resolving
   - Location: SocialNetworks/links.json

4. **BlockTheHate** (בלוק השנאה)
   - URL: https://www.blockthehateil.com/
   - Status: DNS not resolving
   - Location: SocialNetworks/links.json

### Updated URL:

5. **Oct7.App** (אוקט7 - אפילקצית תגובות)
   - Old URL: https://app.oct7.io/ (returned HTTP 404)
   - New URL: https://www.oct7.io/ (working)
   - Location: SocialNetworks/links.json

## Testing Methodology

- Automated testing using curl (10s connection timeout, 15s max timeout)
- Manual verification using web_fetch and browser testing
- Tested against actual websites on February 7, 2026

## Files Changed

- `_data/links/StrategicCommunication/Main/links.json` (1 initiative removed)
- `_data/links/StrategicCommunication/SocialNetworks/links.json` (3 initiatives removed, 1 URL updated)
- `DEAD_LINKS_REPORT_2026-02-07.md` (detailed report added)

## Impact

- Improves user experience by removing links that lead to dead websites
- Reduces frustration for visitors trying to access these resources
- Keeps the database clean and up-to-date

## Notes

- Some sites (e.g., iron-swords.co.il, wordsofiron.com) returned HTTP 403 due to Cloudflare protection but are actually working - these were NOT removed
- Full testing report is included in `DEAD_LINKS_REPORT_2026-02-07.md`
- This is a test run focusing on the Strategic Communication category only

## PR Creation Instructions

To create this PR on GitHub:

1. Visit: https://github.com/4talbot/LinksForIsrael/pull/new/fix/dead-links-strategic-communication-2026-02-07
2. Set base repository: `4tals/LinksForIsrael` base: `main`
3. Set head repository: `4talbot/LinksForIsrael` compare: `fix/dead-links-strategic-communication-2026-02-07`
4. Use the title and description from this document
5. Add labels: `maintenance`, `data-quality`, `dead-links`

## Branch Details

- Branch name: `fix/dead-links-strategic-communication-2026-02-07`
- Fork: 4talbot/LinksForIsrael
- Upstream: 4tals/LinksForIsrael
- Commit: 16aef2a
