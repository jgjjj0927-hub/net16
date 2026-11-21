$env:CLOUDFLARE_API_TOKEN = "твой_токен"
$env:CLOUDFLARE_ACCOUNT_ID = "твой_account_id"

$nodes = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"

foreach ($n in $nodes) {
    $proj = "net16-node-$n"
    Write-Host "деплой $proj..."
    npx wrangler pages deploy "output/node-$n" --project-name $proj
}
