# SETUP_COMMANDS.md

## macOS / Linux / zsh

```bash
mkdir -p personal-engineering-brain/{00-inbox,20-topics,30-themes,50-sources,90-archive,scripts}
mkdir -p personal-engineering-brain/10-news/{markets,software-engineering,ai-engineering,data-engineering,data-science,mlops,llm,ai-research}
mkdir -p personal-engineering-brain/40-summaries/{daily,weekly,monthly}
mkdir -p personal-engineering-brain/templates

cd personal-engineering-brain
git init

printf ".DS_Store\n.env\n.env.*\n!.env.example\n.obsidian/workspace*.json\n" > .gitignore
```

Create a ZIP later:

```bash
cd ..
zip -r personal-engineering-brain.zip personal-engineering-brain \
  -x "*/.git/*" \
  -x "*/.DS_Store"
```

---

## Windows 11 PowerShell

```powershell
$root = "personal-engineering-brain"

$folders = @(
    "$root\00-inbox",
    "$root\10-news\markets",
    "$root\10-news\software-engineering",
    "$root\10-news\ai-engineering",
    "$root\10-news\data-engineering",
    "$root\10-news\data-science",
    "$root\10-news\mlops",
    "$root\10-news\llm",
    "$root\10-news\ai-research",
    "$root\20-topics",
    "$root\30-themes",
    "$root\40-summaries\daily",
    "$root\40-summaries\weekly",
    "$root\40-summaries\monthly",
    "$root\50-sources",
    "$root\90-archive",
    "$root\templates",
    "$root\scripts"
)

$folders | ForEach-Object {
    New-Item -ItemType Directory -Force -Path $_ | Out-Null
}

Set-Location $root
git init
```

Create ZIP:

```powershell
Set-Location ..

Compress-Archive `
  -Path ".\personal-engineering-brain\*" `
  -DestinationPath ".\personal-engineering-brain.zip" `
  -Force
```
