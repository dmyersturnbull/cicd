<!--
Render a jagged grid of badges.
Use line breaks to separate rows, not paragraphs; the latter looks ugly.
In GitHub-flavored Markdown, do this by ending the line with `\` .
The `\` are added on separate `:tyranno:` lines for visibility.
-->
<!-- :tyranno: [![Version status](https://img.shields.io/pypi/status/${.name}?label=Status)](https://pypi.org/project/${.name}) -->
<!-- :tyranno: [![Version on PyPi](https://badgen.net/pypi/v/${.name}?label=PyPi -->
<!-- :tyranno: [![Version on GitHub](https://badgen.net/github/release/${.frag}/stable?label=GitHub)](${.link.repo}/releases) -->
<!-- :tyranno: [![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/cicd?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/${.frag})
               \ -->
<!-- :tyranno: [![Build (Actions)](https://img.shields.io/github/workflow/status/${.name}/${.org}/maintest?label=Tests)](${.link.url}/actions) -->
<!-- :tyranno: [![Coverage (coveralls)](https://badgen.net/coveralls/c/github/${.name}/${.name}?label=Coveralls)](https://coveralls.io/github/${.frag}?branch=main) -->
<!-- :tyranno: [![Coverage (codecov)](https://badgen.net/codecov/c/github/${.frag}?label=CodeCov)](https://codecov.io/gh/${.frag})
               \ -->
<!-- :tyranno: [![Maintainability (Code Climate)](https://badgen.net/codeclimate/maintainability/${.frag})](https://codeclimate.com/github/${.frag}/maintainability) -->
<!-- :tyranno: [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/${.frag}/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/${.frag}/?branch=main) -->
<!-- :tyranno: [![CodeFactor](https://www.codefactor.io/repository/github/${.frag}/badge)](https://www.codefactor.io/repository/github/${.frag})
               \ -->
<!-- :tyranno: [![License](https://badgen.net/pypi/license/${.name}?label=License)](${.license.url}) -->
<!-- :tyranno: [![DOI](https://zenodo.org/badge/DOI/${.doi}.svg)](https://doi.org/${.doi}) -->
<!-- :tyranno: [![Created with ${.Name}](https://img.shields.io/badge/Created_with-${.Name}-0000ff.svg)](https://github.com/${.frag}) -->

[![Version status](https://img.shields.io/pypi/status/tyrannosaurus?label=Status)](https://pypi.org/project/tyrannosaurus)
[![Version on PyPi](https://badgen.net/pypi/v/tyrannosaurus?label=PyPi)](https://pypi.org/project/tyrannosaurus)
[![Version on GitHub](https://badgen.net/github/release/dmyersturnbull/tyrannosaurus/stable?label=GitHub)](https://github.com/dmyersturnbull/tyrannosaurus/releases)
[![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/tyrannosaurus?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/dmyersturnbull/tyrannosaurus)
[![Build (Actions)](https://img.shields.io/github/actions/workflow/status/dmyersturnbull/tyrannosaurus/push-main.yml?label=Tests)](https://github.com/dmyersturnbull/tyrannosaurus/actions)
[![Coverage (coveralls)](https://badgen.net/coveralls/c/github/dmyersturnbull/tyrannosaurus?label=Coveralls)](https://coveralls.io/github/dmyersturnbull/tyrannosaurus?branch=main)
[![Coverage (codecov)](https://badgen.net/codecov/c/github/dmyersturnbull/tyrannosaurus?label=CodeCov)](https://codecov.io/gh/dmyersturnbull/tyrannosaurus)\
[![Maintainability (Code Climate)](https://badgen.net/codeclimate/maintainability/dmyersturnbull/tyrannosaurus)](https://codeclimate.com/github/dmyersturnbull/tyrannosaurus/maintainability)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/tyrannosaurus/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/tyrannosaurus/?branch=main)
[![CodeFactor](https://www.codefactor.io/repository/github/dmyersturnbull/tyrannosaurus/badge)](https://www.codefactor.io/repository/github/dmyersturnbull/tyrannosaurus)\
[![License](https://badgen.net/pypi/license/tyrannosaurus?label=License)](https://opensource.org/licenses/Apache-2.0)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4485186.svg)](https://doi.org/10.5281/zenodo.4485186)
[![Created with Tyrannosaurus](https://img.shields.io/badge/Created_with-Tyrannosaurus-0000ff.svg)](https://github.com/dmyersturnbull/tyrannosaurus)

# Sandbox for Tyrannosaurus

This is the prototype next-gen [tyrannosaurus](https://github.com/dmyersturnbull/tyrannosaurus).
When ready, that repository will be updated.

> [!CAUTION]
> :**🚧 Status:** The GitHub workflows and installable CLI package under construction.

**A template for post-modern Python projects**
built with
[Hatch](https://hatch.pypa.io/),
[uv](https://docs.astral.sh/uv/),
[mkdocs-material](https://squidfunk.github.io/mkdocs-material/),
[Ruff](https://github.com/astral-sh/ruff),
and [GitHub actions](https://docs.github.com/en/actions).

### 🎁 Features

Autoformatting,
[conventional commits](https://www.conventionalcommits.org/) and
[autogenerated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes),
publishing to PyPi + container registries + GH Releases + GH Pages,
reports to [Coveralls](https://coveralls.io/) + [Codecov](https://codecov.io/) + etc.,
and some [advanced CI/CD workflows](https://github.com/dmyersturnbull/cicd/blob/main/.github/workflows).
It’s also an installable package that finds `:tyranno:` comments in yaml, toml, Python, etc.
Want to use your pyproject.toml `project.description` in your readme?
Use `<!-- :tyranno: ${project.description} -->`

_Everything is optional._
Not using Docker? Delete `Dockerfile`. The workflows will skip it.
Hate all the GitHub workflows? Delete them.
There’s no magic anywhere.
Only standard tools are used, and they’re used in transparent ways.
Just clone this repo and start modifying as you see fit.

> [!TIP]
> :**Making a repo supporting a scientific publication?**
> Tyrannosaurus has a little sister,
> [science-notebook-template 🧪](https://github.com/dmyersturnbull/science-notebook-template).

### 🎨 Another `sync` example

Maybe you want your GitHub workflows to use your `pyproject.toml` Python version.
Set `default-python-version` in `[tool.tyranno.data]` and reference it:

```yaml
- uses: astral-sh/setup-uv@v5
  with:
    # :tyranno: python-version: "${.default-python-version|vr_minor(@)}"
    python-version: "3.13"
```

If you wanted, you could define `default-python-version` dynamically, too.
Use [JMESPath](https://jmespath.org/) to find the max version compatible with `requires-python`:

```toml
[project]
requires-python = ">=3.11,<4.0"

[tool.tyranno.data]
# uses two custom functions that Tyranno provides: vrspec_filter and vr_max
# :tyranno: default-python-version = "${project.requires-python|vrspec_filter('python',@)|vr_max(@)}"
default-python-version = "3.13.1"
```

### ✏️ How to start

First, [install uv](https://docs.astral.sh/uv/getting-started/installation/).
I also recommend [just](https://github.com/casey/just)
and the
[GitHub CLI](https://cli.github.com/).

1. Clone this repo with `git clone` or
   ["Use this template"](https://github.com/new?template_name=cicd&template_owner=dmyersturnbull).
2. Edit `pyproject.toml` as needed, mainly the `[project]` and `[tool.tyranno.data]` sections.
3. Add or remove any files as you see fit.
   For example, if you don’t use Docker, delete `Dockerfile` and `compose.yaml`.
4. Add your code to `src/` and `tests/`.
   (Consider keeping the `_about.py`.)
5. Run `just lock` uvx pre-commit install`, and `uvx pre-commit --all-files`.

Do whatever after that.
I recommend a PR-only workflow, and using
[conventional commits](https://www.conventionalcommits.org/)
with the commit types listed in [`release.yaml`](.github/release.yaml)
(full labels in [`project.yaml`](.github/project.yaml)).
This enables beautiful
[autogenerated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes).
[Release Drafter](https://github.com/release-drafter/release-drafter)
is a popular alternative to GitHub’s feature.

### 🍁 Contributing

New issues and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/cicd/blob/master/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/cicd/blob/main/SECURITY.md).

```text
                    __
                   / _)
        _.----._/ /  _ ,
  .___/        / / = = ,
:----- | ) - ( |
       : :   : :
```

<small>It’s a <s>turtle with arms.</s> <s>dog.</s> <s>misshapen mango?</s> T-rex.</small>
