
# Medicare Documentation

This repository holds documentation on the Medicare data held at the NBER.


## Developing

### Adding documentation

All the documentation is written in markdown format. [Here's](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) a helpful cheatsheet for how to do formatting in markdown. It's all really intuitive.

The site layout is determined by the `pages` section of [`mkdocs.yml`](mkdocs.yml):


```yaml
pages:
    - Home: 'index.md'
    - NBER Documentation:
        - Overview: 'NBER_website/1_Overview.md'
        - Description of Claims Files: 'NBER_website/2_Background.md'
        - Getting Started with SAS: 'NBER_website/3_Getting_started_with_SAS.md'
        - Constructing Extracts with SAS: 'NBER_website/4_constructing_extracts.md'
        - Manipulating Extracts with SAS: 'NBER_website/5_manipulating_medicare_extracts.md'
        - Generating Costs Measures: 'NBER_website/6_costs.md'
        - References: 'NBER_website/7_references.md'
        - Appendix: 'NBER_website/8_appendix.md'
    - ResDAC Documentation:
        - Beneficiary Summary File: 'resdac/mbsf.md'
        - Carrier RIF: 'resdac/carrier-rif.md'
        - Denominator RIF: 'resdac/denominator-rif.md'
        - Durable Medical Equipment RIF: 'resdac/dme-rif.md'
        - Home Health Agency RIF: 'resdac/hha-rif.md'
        - Hospice RIF: 'resdac/hospice-rif.md'
        - Inpatient RIF: 'resdac/ip-rif.md'
        - MedPAR RIF: 'resdac/medpar-rif.md'
        - Outpatient RIF: 'resdac/op-rif.md'
        - Skilled Nursing Facility RIF: 'resdac/snf-rif.md'
        - Variable Definitions: 'resdac/variables.md'
    - Working with the Data:
        - Goals for New Data Format: 'kyle/goals-for-modern-data-format.md'
        - Standard Readme: 'kyle/01medicare_readme.md'
        - Data Extraction Overview: 'kyle/extract_data.md'
        - Data Locations: 'kyle/data_locations.md'
        - Python Extraction: 'kyle/python_extract.md'
        - Using tmux for long-running jobs: 'kyle/using-tmux-aging-servers.md'
    - Important Details:
        - Enrollment Restrictions: 'mauricio/enrollment-restrictions.md'
        - Calculating Costs for Inpatient Visits: 'mauricio/lag-post-event-spending.md'
    - Glossary: 'glossary.md'
```

This layout is subject to change.

- NBER Documentation: Files ported from the [NBER website](https://www.nber.org/medicare/public/Public.html)
- ResDAC Documentation: Files scraped from [ResDAC](https://www.resdac.org/). The [`resdac-scrape.py`](resdac-scrape.py) program scrapes the website and automatically populates the files in `docs/resdac/`. Therefore, **don't edit any files in `docs/resdac/`** as your edits will be overwritten.
- The rest of the files are currently a mish mash.

### Serving the site locally

This website uses [`mkdocs`](http://www.mkdocs.org/), a Markdown site generator, with the [`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/) theme. To serve the site locally, first make sure you have Python 3 installed, and then do:

```
$ pip install mkdocs mkdocs-material
```

If you're at the top-level folder, with the `mkdocs.yml` file in the current directory, you can do `mkdocs serve` and the website will be running at `localhost:8000`. So open up your web browser, type in `localhost:8000`, click enter, and the site will appear.



You can also do `mkdocs --help` to see all available commands.

```
> mkdocs --help
Usage: mkdocs [OPTIONS] COMMAND [ARGS]...

  MkDocs - Project documentation with Markdown.

Options:
  -V, --version  Show the version and exit.
  -q, --quiet    Silence warnings
  -v, --verbose  Enable verbose output
  -h, --help     Show this message and exit.

Commands:
  build      Build the MkDocs documentation
  gh-deploy  Deploy your documentation to GitHub Pages
  new        Create a new MkDocs project
  serve      Run the builtin development server
```


