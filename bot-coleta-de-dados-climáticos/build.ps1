$exclude = @("venv", "bot-coleta-de-dados-climáticos.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-coleta-de-dados-climáticos.zip" -Force