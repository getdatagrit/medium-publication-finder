# Medium Publication Finder: Subscribers & Activity

Find Medium publications by keyword and score each one: subscribers, posting cadence, claps per post, paywalled share and top authors.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/medium-publication-finder) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/medium-publication-finder/)

**from $3.50 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

Medium Publication Finder turns a keyword (or a list of publication names) into one scorecard row per Medium publication: how many people follow it, how often it posts, when it last posted, how many claps a typical story gets, how much of it sits behind the paywall, and who writes for it.
It reads the public data Medium serves to any visitor, so there is no login, no API key and no Medium account involved. Export the rows as JSON, CSV or Excel, call the Actor through the Apify API, or connect it to n8n, Make and AI agents through MCP.

## Quick start

1. Open [Medium Publication Finder: Subscribers & Activity on Apify Store](https://apify.com/datagrit/medium-publication-finder) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "queries": [
    "startup",
    "machine learning"
  ],
  "maxPublicationsPerQuery": 8,
  "maxItems": 16
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `queries` | array | Keywords to search Medium publications for, one per line (for example "startup" or "machine learning"). Each keyword is searched separately and the publications it returns are scored. |
| `publications` | array | Specific publications to score: a slug (better-programming), a link (https://medium.com/swlh) or a custom domain (uxdesign.cc). Profiles of people (@name) are not publications and are ignored. |
| `maxPublicationsPerQuery` | integer | How many publications to score for each search keyword, in the order Medium ranks them. Publications outside the subscriber range do not count toward this number. |
| `postsSample` | integer | How many of a publication's most recent posts feed the cadence and engagement figures, 5 to 25. Medium serves at most 25 per publication. |
| `minSubscribers` | integer | Skip publications with fewer followers than this. 0 means no minimum. Skipped publications are not charged. |
| `maxSubscribers` | integer | Skip publications with more followers than this, which is useful for finding smaller publications that answer pitches. 0 means no maximum. |
| `activeWithinDays` | integer | Keep only publications whose newest post is at most this many days old, which drops dormant publications with large follower counts. 0 means no limit. Publications without posts are skipped when this is set. |
| `maxItems` | integer | Stop after this many publication rows in total across all keywords and direct lookups. |
| `proxyConfiguration` | object | Optional proxy. Leave disabled unless Medium refuses requests from your region; residential proxy raises the platform cost of the run. |

## Output

| Field | Type | Description |
|---|---|---|
| `query` | string | The search keyword or publication entry this row belongs to. |
| `id` | string | Medium identifier of the publication. Empty only on the status row. |
| `slug` | string | Publication slug as used in medium.com/<slug>. Empty only on the status row. |
| `name` | string | Publication name. Empty only on the status row. |
| `url` | string | Public address of the publication: its custom domain when it has one, otherwise medium.com/<slug>. |
| `customDomain` | string | Custom domain the publication is served from, or null when it lives on medium.com. |
| `tagline` | string | One-line tagline shown on the publication page. |
| `description` | string | Full description written by the publication owners. |
| `subscribers` | integer | Number of Medium users following the publication. |
| `creatorUsername` | string | Medium username of the account that created the publication. |
| `creatorName` | string | Display name of the account that created the publication. |
| `editorsCount` | integer | Number of editors listed for the publication. Editors are the people who accept or reject submissions. |
| `editors` | array | Editors with their Medium username and display name. |
| `twitterUsername` | string | Twitter/X handle the publication lists, or null. |
| `newsletterSlug` | string | Slug of the publication newsletter on Medium, or null when it has none. |
| `postsSampled` | integer | Number of recent posts that feed the metrics below; 0 means the publication has no posts, null means Medium did not return the list. |
| `sampleSpanDays` | number | Days between the oldest analysed post and the time of the run. |
| `lastPostAt` | string | ISO 8601 date of the newest analysed post. |
| `daysSinceLastPost` | number | Days between the newest analysed post and the time of the run. |
| `postsPerWeek` | number | Posts per week over the analysed sample, measured up to the time of the run, so a publication that stopped posting scores low. |
| `activityStatus` | string | active when the newest post is at most 14 days old, slowing up to 60 days, dormant beyond that, empty when the publication has no posts. |
| `medianClaps` | number | Median clap count per analysed post. |
| `averageClaps` | number | Mean clap count per analysed post. |
| `medianClapsPer1kSubscribers` | number | Median claps divided by subscribers, times 1,000; compares engagement between publications of different sizes. |
| `medianResponses` | number | Median number of responses (comments) per analysed post. |
| `medianReadingMinutes` | number | Median reading time in minutes of the analysed posts. |
| `medianWords` | integer | Median word count of the analysed posts. |
| `memberOnlySharePct` | number | Share of analysed posts that sit behind the Medium paywall, in percent. |
| `distinctAuthors` | integer | Number of different authors among the analysed posts; 1 means a one-person publication. |
| `topAuthors` | array | Up to three authors with the most analysed posts: username, name and post count. |
| `topTags` | array | Up to five tags used most often across the analysed posts, with post counts. |
| `bestPost` | object | The analysed post with the most claps: title, URL and clap count. |
| `found` | boolean | False only for status rows (no match, publication not found, request failed, filtered out). |
| `reason` | string | Present on status rows only: noMatches, filteredOut, notFound or fetchFailed. |
| `message` | string | Present on status rows only: what happened and what to change. |
| `sourceUrl` | string | Public page of the publication the row was read from. |
| `scrapedAt` | string | ISO 8601 timestamp of extraction. |

Sample record:

```json
{
  "query": "startup",
  "id": "f5af2b715248",
  "slug": "swlh",
  "name": "The Startup",
  "url": "https://medium.com/swlh",
  "customDomain": "uxdesign.cc",
  "tagline": "Get smarter at building your thing.",
  "description": "Get smarter at building your thing. Follow to join The Startup’s +8 million monthly readers.",
  "subscribers": 894499,
  "creatorUsername": "meseali",
  "creatorName": "Ali Mese",
  "editorsCount": 2,
  "editors": [
    {
      "username": "meseali",
      "name": "Ali Mese"
    }
  ],
  "twitterUsername": "GrowthSupply",
  "newsletterSlug": "top-stories",
  "postsSampled": 25,
  "sampleSpanDays": 175.3,
  "lastPostAt": "2026-05-25T19:56:00.532Z",
  "daysSinceLastPost": 134.6,
  "postsPerWeek": 1,
  "activityStatus": "dormant",
  "medianClaps": 412,
  "averageClaps": 380.5,
  "medianClapsPer1kSubscribers": 0.46,
  "medianResponses": 8,
  "medianReadingMinutes": 5.6,
  "medianWords": 1024,
  "memberOnlySharePct": 68,
  "distinctAuthors": 22,
  "topAuthors": [
    {
      "username": "aldric-chen",
      "name": "Aldric Chen",
      "posts": 3
    }
  ],
  "topTags": [
    {
      "tag": "productivity",
      "posts": 6
    }
  ],
  "bestPost": {
    "title": "These Countries Offer Real Estate Visas",
    "url": "https://medium.com/swlh/example-396cb0c83ba2",
    "claps": 474
  },
  "found": true,
  "reason": "filteredOut",
  "message": "Publications were found but none passed the subscriber and activity filters.",
  "sourceUrl": "https://medium.com/swlh",
  "scrapedAt": "2026-10-07T08:00:00.000Z"
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~medium-publication-finder/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries":["startup","machine learning"],"maxPublicationsPerQuery":8,"maxItems":16}'
```

## FAQ

**Why is a publication missing from my results?**  
Either Medium search did not return it for your keyword, or it was removed by your subscriber or activity filters. If every publication is removed you get one `filteredOut` row explaining it.

**Why are median claps zero?**  
Many publications get few claps. Look at `averageClaps` and `bestPost` to see whether a few stories carry the engagement. A missing value is never reported as zero: if Medium returns no clap count for any post, the field is `null` and the status message shows the clap-count coverage.

**Does it return articles?**  
No. It scores publications. Use an article scraper when you need story text.

**How fresh is the data?**  
Every run reads Medium live.

**Can I schedule runs?**  
Yes, use Apify schedules to track how follower counts and cadence change.

**Something looks wrong.**  
Open an issue with the input you used; layout changes at Medium are fixed quickly.

## More from datagrit

- [Bilibili Anime Catalog, Rankings & Calendar](https://github.com/getdatagrit/bilibili-anime-series-tracker) - Bilibili anime, Chinese animation, film, documentary and TV series: filterable catalog, Top 100 rankings, release calendar and season details with ratings and follower counts.
- [Bluesky Community Finder: Starter Packs & Feeds](https://github.com/getdatagrit/bluesky-community-finder) - Find Bluesky starter packs, custom feeds and curated lists by topic, with join counts, feed likes and full member lists with follower counts.
- [Substack Newsletter Sponsorship Prospect Finder](https://github.com/getdatagrit/substack-sponsor-prospector) - Substack publications ranked for sponsorship: subscriber count, paid-tier size, plan prices, posting cadence and engagement per 1,000 subscribers.
- [Telegram Channel Analytics: Growth and Reach](https://github.com/getdatagrit/telegram-channel-growth-analytics) - One row per public Telegram channel: subscribers and growth since your last run, median views, view rate, posting cadence, reactions and forward sources.
- [TED Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/ted-contract-expiry-radar) - Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/medium-publication-finder). Examples are MIT licensed.
