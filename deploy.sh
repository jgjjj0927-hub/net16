#!/bin/bash
export CLOUDFLARE_API_TOKEN="твой_токен"
export CLOUDFLARE_ACCOUNT_ID="твой_account_id"

for n in a b c d e f g h i j k l m n o p; do
    proj="net16-node-$n"
    echo "деплой $proj..."
    npx wrangler pages deploy "output/node-$n" --project-name "$proj"
done
