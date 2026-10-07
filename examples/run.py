# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/medium-publication-finder").call(run_input={
    "queries": [
        "startup",
        "machine learning"
    ],
    "maxPublicationsPerQuery": 8,
    "maxItems": 16
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
