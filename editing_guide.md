# Repository Editing Guide

This document explains how the repository is structured and how to edit its contents.  
All Climate Compatible Growth (CCG) tool websites (for example, MAED, FFRM, OSeMOSYS) follow the same structure.

---

## `_config.yml`

This is the main configuration file for the site.

It defines:
- Site title, description, and base URL  
- Theme (`jekyll-theme-primer`)  
- Navigation menus and site-wide links  
- Plugin settings and metadata  

Edit this file only to:
- Update the site title or description  
- Add or remove navigation items  
- Change theme or high-level configuration  

Reference: [Jekyll Config Documentation](https://jekyllrb.com/docs/configuration/)

---

## `index.html`

This is the home page of the website.  
It controls what visitors see first—such as the banner, summary text, and featured sections.

Edit this file to:
- Update homepage text and links  
- Change featured cards or sections  
- Adjust visuals or intro formatting  

Reference: [Editing Jekyll Pages](https://jekyllrb.com/docs/pages/)

---

## Subpages

Subpages are written in Markdown, which makes them easy to update.

| File | Purpose |
|------|----------|
| `about.markdown` | Overview of the tool, its history, and objectives |
| `application.markdown` | Describes how the tool is applied and includes recommended readings |
| `learning_capacity.markdown` | Lists EMP training and capacity-building events (data-driven from `_data/learning_events.yml`) |
| `get_involved.markdown` | Describes ways to collaborate, contribute, or join the community |
| `dataset.markdown` | *(Archived)* Previously used for describing datasets |

Reference: [Markdown Guide](https://www.markdownguide.org/basic-syntax/)  
You can also use basic HTML inside Markdown for finer control (for example, custom formatting or image placement).

---

## `_layouts/`

This folder defines standard page templates.

| Layout | Description |
|---------|--------------|
| `home.html` | Used by the homepage (`index.html`) |
| `sub-page.html` | Template for About, Applications, and other content pages |
| `support-page.html` | Layout for help or resource sections |
| `form-page.html` | Used for forms (if applicable) |

These layouts automatically pull in the header, footer, and shared styles.

Reference: [Layouts in Jekyll](https://jekyllrb.com/docs/layouts/)

---

## `_includes/`

Contains reusable content blocks used across multiple pages.

| Include | Description |
|----------|--------------|
| `header.html` | Navigation bar |
| `footer.html` | Footer with partner logos and contact info |
| `coming_soon.html` | Standard placeholder for in-progress pages |
| `subpage_links.html` | Adds navigation links between subpages |

You can insert these blocks anywhere using:
```liquid
{% include header.html %}

Reference: [Includes in Jekyll](https://jekyllrb.com/docs/includes/)

## `_data/`

Stores structured content in YAML format.  
This makes it easy to update lists and dynamic content without editing HTML.

| File | Description |
|------|--------------|
| `learning_events.yml` | Data for EMP events and adjacent workshops displayed on the Learning page |
| `publications.yml` | Recommended readings shown under Applications |
| `social_media.yml` | Social media links in the footer |
| *(Optional)* `rgs.yml` | Partner institutions associated with the tool |

Reference: [Working with Data Files](https://jekyllrb.com/docs/datafiles/)

---

## `assets/img/`

Holds all images used on the website.

**Subfolders:**
- `/EMP/` – Photos from EMP and related capacity-building events  
- `/partners/` – Logos of collaborating organisations (for example, IAEA, IRENA)  
- `/img/` – Tool logos, backgrounds, icons, and general visuals  

Event image names should match their YAML entries (for example, `EMP-A 2025.jpg`).

---

## Styling

Located at `assets/css/custom.scss`

This file controls the styling and visual identity of the site, including colours, fonts, spacing, and animations.

All sites share a standard format, but you can modify styles to suit your tool’s branding.

Reference: [Sass/SCSS Guide](https://sass-lang.com/guide)

---

## Gemfiles

| File | Description |
|------|--------------|
| `Gemfile` | Lists Ruby and Jekyll dependencies |
| `Gemfile.lock` | Automatically generated after installation |

These files are used to build and run the Jekyll site locally.

To install and preview:

```bash
bundle install
bundle exec jekyll serve

Reference: [Jekyll Installation](https://jekyllrb.com/docs/installation/)

## `README.md`

This file appears on the GitHub repository’s main page.

Use it to:
- Summarize the purpose of the repository  
- Add links to the live site  
- Include contact or contribution information  

---

## YAML Data Example

To keep pages tidy, structured data such as event details are stored in YAML files.  
Example from `learning_events.yml`:

```yaml
- title: "EMP-A 2025 – Addis Ababa, Ethiopia"
  image: "/assets/img/EMP/EMP-A 2025.jpg"
  description: "Hosted at UNECA, five national teams developed models..."
  outputs:
    - country: "Rwanda"
      title: "Forecasting Final Energy Demand"
      url: "https://zenodo.org/records/15364342"

Reference: [YAML Basics](https://yaml.org/spec/)

Editing and Submitting Changes

Follow these steps to safely edit and submit updates to the repository:

Fork this repository on GitHub.

Create a branch for your edits:

git checkout -b update-learning-page


Edit the .markdown or .yml files as needed.

Commit your changes with a clear message:

git add .
git commit -m "Updated EMP-A 2025 event details"


Push your branch to your fork:

git push origin update-learning-page


Open a Pull Request on GitHub to propose your changes.

Reference: Creating a Pull Request

Summary of Folder Structure
| Folder/File | Purpose |
|--------------|----------|
| `_config.yml` | Main site configuration |
| `index.html` | Homepage |
| `about.markdown` | About the tool |
| `application.markdown` | Applications and case studies |
| `learning_capacity.markdown` | EMP and capacity building events |
| `get_involved.markdown` | Collaboration and contribution details |
| `_layouts/` | Page templates |
| `_includes/` | Shared components like header and footer |
| `_data/` | Structured data files (events, partners, publications) |
| `assets/img/` | Images and logos |
| `assets/css/custom.scss` | Styling |
| `Gemfile`, `Gemfile.lock` | Build dependencies |
| `README.md` | Repository overview on GitHub |
| `editing_guide.md` | Internal guide for editors (this document) |


## Previewing Your Changes Locally

You can test your edits locally before submitting them.

Open a terminal in the repository folder.

Run the following commands:

bundle install
bundle exec jekyll serve


Open your browser and go to:

http://localhost:4000


This will let you preview the site as it would appear once published.