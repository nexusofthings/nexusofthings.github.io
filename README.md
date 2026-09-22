# nexusofthings.github.io

Personal site built with [Quarto](https://quarto.org), modelled on other publicly available sites to document my academic and personal information (and of course, with the help of AI). 

It rebuilds and deploys on every push.

## Preview locally

Install [Quarto](https://quarto.org/docs/get-started/), then from this folder:

```bash
quarto preview        # live-reloading preview in your browser
quarto render         # full build into _site/
```

## Go live (replacing the old Jekyll site)

```bash
# 1. Keep the old site on its own branch, just in case
git clone https://github.com/nexusofthings/nexusofthings.github.io
cd nexusofthings.github.io
git checkout -b jekyll-archive && git push -u origin jekyll-archive
git checkout main

# 2. Replace everything with this project
git rm -r -q .
#    copy the contents of this folder in (including the hidden .github/ and .gitignore)
git add -A && git commit -m "Rebuild site with Quarto" && git push
```

3. On GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Open the **Actions** tab. "Publish site" runs on the push (re-run it if it ran before you changed the setting in step 3).

Also replace the README in your profile repo (`nexusofthings/nexusofthings`) with `github-profile/README.md`.

Old links such as `/all-about-funding/` and `/about/` redirect to the new pages.

## Before you publish: make it yours

| What | Where |
|---|---|
| Your name | `_quarto.yml` (`title:` and footer) and `_variables.yml` |
| Hero text, chips, buttons | `index.qmd` |
| Whether your employer appears | `_variables.yml` (`affiliation`), `index.qmd`, `data/experience.yml` |
| Research and Teaching wording (drafts, edit freely) | `research.qmd`, `data/teaching.yml` |
| LinkedIn / ORCID / Scholar icons | uncomment the examples in `_quarto.yml` (navbar `tools:`) and `index.qmd` (hero buttons) |
| Photo | replace `assets/bio-photo.webp` (square, about 640 px). The current image is the network graph from your old site; if you did not make it yourself, check its licence and credit it, or swap in your own picture |

## Everyday updates

| To add... | Edit | Then |
|---|---|---|
| A publication | `data/publications.yml` | commit and push |
| A talk, poster or workshop | `data/conferences.yml` | commit and push |
| A role | `data/experience.yml` | commit and push |
| A course or workshop | `data/teaching.yml` | commit and push |
| A blog post | `python scripts/new.py post "Title" -c R` | write it, delete the `draft: true` line, push |
| A short note | `python scripts/new.py note "Title"` | same |
| A repo on the Software page | nothing: new public repos appear automatically each week | to describe one by hand, add its name to `data/featured_repos.txt` and write it up in `software.qmd` |

The CV page is assembled from the same YAML files, so it updates itself. Use the browser's print dialog to save it as a PDF.

**YAML tips.** Copy an existing block and edit it. Text fields accept `**bold**`, `*italic*` and `[link text](https://...)`.
Put your own name in bold in `authors`. In `publications.yml` and `conferences.yml` the example block has a
`hidden: true` line; delete that line to publish it. A misplaced indent is the usual cause of a build error,
and the error message names the line.

## What runs automatically

| Workflow | When | What it does |
|---|---|---|
| `publish.yml` | every push to `main`, every Monday, or by hand | refreshes the GitHub repo list, renders the site, deploys to Pages |
| `monthly-reminder.yml` | 1st of each month | opens an issue with an update checklist (`.github/monthly-checklist.md`) |

## Posts with R code

Code in fenced blocks (` ```r `) is shown, not run. To run code and show its output, use ` ```{r} `, run
`quarto render` on your own machine (needs R and `knitr`), and commit the `_freeze/` folder. The build on GitHub
then reuses those results and needs no R. `freeze: auto` in `_quarto.yml` is what makes this work.

## Drafts

Any post with `draft: true` is left out of the site, the blog listing, the RSS feed, search and the sitemap (a
draft's URL exists only as a blank page). Your nine unfinished notes from the old site are kept this way in
`blog/posts/` and `notes/posts/`. Delete the `draft: true` line from one to publish it. `random-thoughts` is
personal, so decide whether it belongs on a professional site.

## If you edit the listing templates

The four files in `templates/` turn the YAML into HTML. Two Quarto quirks are documented at the top of each:
in Quarto's EJS the "equals" output tag prints raw HTML (the reverse of stock EJS), and the output must have
one element per line with no blank lines or indentation, or Quarto's markdown parser turns it into a code block.
