<!--
Render a jagged grid of badges.
Use line breaks to separate rows, not paragraphs; the latter looks ugly.
In GitHub-flavored Markdown, do this by ending the line with `\` .
-->
<!-- :tyranno: [![Version status](https://img.shields.io/pypi/status/${{project.name}}?label=Status)](https://pypi.org/project/${{project.name}})-->
<!-- :tyranno: [![Version on PyPi](https://badgen.net/pypi/v/${{project.name}}?label=PyPi)-->
<!-- :tyranno: [![Version on GitHub](https://badgen.net/github/release/${{.frag}}/stable?label=GitHub)](${{.frag}}/releases)-->
<!-- :tyranno: [![Version on Docker Hub](https://img.shields.io/docker/v/${{.frag}}?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/${{.frag}})\-->
<!-- :tyranno: [![Build (Actions)](https://img.shields.io/github/workflow/status/${{.frag}}/test?label=Tests)](${{.frag}}/actions)-->
<!-- :tyranno: [![Coverage (coveralls)](https://badgen.net/coveralls/c/github/${{project.name}}/${{project.name}}?label=Coveralls)](https://coveralls.io/github/${{.frag}}?branch=main)-->
<!-- :tyranno: [![Coverage (codecov)](https://badgen.net/codecov/c/github/${{.frag}}?label=CodeCov)](https://codecov.io/gh/${{.frag}})\-->
<!-- :tyranno: [![Maintainability (Code Climate)](https://badgen.net/codeclimate/maintainability/${{.frag}})](https://codeclimate.com/github/${{.frag}}/maintainability)-->
<!-- :tyranno: [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/${{.frag}}/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/${{.frag}}/?branch=main)-->
<!-- :tyranno: [![CodeFactor](https://www.codefactor.io/repository/github/${{.frag}}/badge)](https://www.codefactor.io/repository/github/${{.frag}})\-->
<!-- :tyranno: [![License](https://badgen.net/pypi/license/${{project.name}}?label=License)](${{project.license.url}})-->
<!-- :tyranno: [![DOI](https://zenodo.org/badge/DOI/${{.doi}}.svg)](https://doi.org/${{.doi}})-->
<!-- :tyranno: [![Created with Tyrannosaurus](https://img.shields.io/badge/Created_with-tyranno-sandbox-0000ff.svg)](https://github.com/${{.frag}})-->

[![Version status](https://img.shields.io/pypi/status/tyranno-sandbox?label=Status)](https://pypi.org/project/tyranno-sandbox)
[![Version on PyPi](https://badgen.net/pypi/v/tyranno-sandbox?label=PyPi)](https://pypi.org/project/tyranno-sandbox)
[![Version on GitHub](https://badgen.net/github/release/dmyersturnbull/tyranno-sandbox/stable?label=GitHub)](https://github.com/dmyersturnbull/tyranno-sandbox/releases)
[![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/tyranno-sandbox?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/dmyersturnbull/tyranno-sandbox)
[![Build (Actions)](https://img.shields.io/github/actions/workflow/status/dmyersturnbull/tyranno-sandbox/push-main.yml?label=Tests)](https://github.com/dmyersturnbull/tyranno-sandbox/actions)
[![Coverage (coveralls)](https://badgen.net/coveralls/c/github/dmyersturnbull/tyranno-sandbox?label=Coveralls)](https://coveralls.io/github/dmyersturnbull/tyranno-sandbox?branch=main)
[![Coverage (codecov)](https://badgen.net/codecov/c/github/dmyersturnbull/tyranno-sandbox?label=CodeCov)](https://codecov.io/gh/dmyersturnbull/tyranno-sandbox)\
[![Maintainability (Code Climate)](https://badgen.net/codeclimate/maintainability/dmyersturnbull/tyranno-sandbox)](https://codeclimate.com/github/dmyersturnbull/tyranno-sandbox/maintainability)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/tyranno-sandbox/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/tyranno-sandbox/?branch=main)
[![CodeFactor](https://www.codefactor.io/repository/github/dmyersturnbull/tyranno-sandbox/badge)](https://www.codefactor.io/repository/github/dmyersturnbull/tyranno-sandbox)\
[![License](https://badgen.net/pypi/license/tyranno-sandbox?label=License)](https://opensource.org/licenses/Apache-2.0)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4485186.svg)](https://doi.org/10.5281/zenodo.4485186)
[![Created with Tyrannosaurus](https://img.shields.io/badge/Created_with-Tyrannosaurus-0000ff.svg)](https://github.com/dmyersturnbull/tyranno-sandbox)

# Sandbox for Tyrannosaurus

This is the prototype next-gen [tyranno-sandbox](https://github.com/dmyersturnbull/tyranno-sandbox).
When ready, that repository will be updated.

> [!CAUTION]
> :**🚧 Status:** The GitHub workflows and installable CLI package under construction.

**A template for post-modern Python projects**
built with
[uv](https://docs.astral.sh/uv/),
[Hatch](https://hatch.pypa.io/),
[Ruff](https://github.com/astral-sh/ruff),
[GitHub actions](https://docs.github.com/en/actions), and
[mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

### 🎁 Features

Autoformatting,
[conventional commits](https://www.conventionalcommits.org/) and
[autogenerated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes),
publishing to PyPi + container registries + GH Releases + GH Pages,
reports to [Coveralls](https://coveralls.io/) + [Codecov](https://codecov.io/) + etc.,
and [solid CI/CD workflows](https://github.com/dmyersturnbull/tyranno-sandbox/blob/main/.github/workflows).

#### It’s opinionated but completely flexible.

**Everything is optional.**
Not using Docker? Delete `Dockerfile`.
Hate all the GitHub workflows? Delete them.

**There’s no magic anywhere.**
Only standard tools are used, and they’re used in transparent ways.

**It uses modern and carefully chosen integrations.**
You don’t need to do the research, prototyping, and testing to determine
the best tools and ensure they coexist peacefully.
Over 100 hours already went into what’s here.

#### There’s an optional `tyranno` command.

`tyrannosaurus` is also an installable package (in this repo: it’s bootstrapped with its own template).
To use it, list `tyrannosaurus` in your dev dependencies (`dependency-groups`).
The CLI is invoked as `tyranno`.
**The `tyranno sync` subcommand** finds specially formatted comments in target globs (`tool.tyranno.targets`).
For example, assuming you’ve listed `README.md` as a target:

```markdown
<!-- :tyranno: ${{project.description}} -->

This next line is the string from pyproject.toml.

<!-- :tyranno: By ${{project.authors[*].name|sort(@)|join(', ', @}} -->

By Kerri Johnson, Henry Chen
```

You can use
[JMESPath community](https://jmespath.site/)
expressions as seen above.
Multiple lines can also be replaced; see below for details.

**The other subcommands** are

- `tyranno rex` or `tyranno reqs` to bump minimum dependency versions in `project` and `dependency-groups`,
- `tyranno req` to search for info about a package such as its changelog or release notes,
- `tyranno trash` to remove unwanted files (globs under `tool.tyranno.trash`),
- `tyranno new` to generate new projects interactively,
- and `tyranno help` for usage.

### ✏️ How to start

> [!TIP]
> :**Making a repo supporting a scientific publication?**
> Tyrannosaurus has a little sister,
> [science-notebook-template 🧪](https://github.com/dmyersturnbull/science-notebook-template).

First, [install uv](https://docs.astral.sh/uv/getting-started/installation/).
I also recommend installing [just](https://github.com/casey/just) (`uv tool install just`)
and the [GitHub CLI](https://cli.github.com/)
_([installation](https://github.com/cli/cli#installation))_.

Create a new project however you normally would.
Or:

1. Clone this repo.
2. Edit `pyproject.toml` as needed, especially `[project]` and `[tool.tyranno.data]`.
3. Add or remove any files as you see fit.
   For example, if you don’t use Docker, delete `Dockerfile`.
4. Add your code to `src/` and `tests/`.
5. Run `just init`.

I recommend a PR-only workflow, and using
[conventional commits](https://www.conventionalcommits.org/)
with the commit types listed in [`release.yaml`](.github/release.yaml)
(full labels in [`project.yaml`](.github/project.yaml)).
This enables
[autogenerated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes).
[Release Drafter](https://github.com/release-drafter/release-drafter)
is a popular alternative to GitHub’s feature.

### 🎨 More on `sync`

Maybe you want your GitHub workflows to use your `pyproject.toml` Python version.
Define `main-python-version` in `[tool.tyranno.data]`
and reference it in a
[JMESPath community](https://jmespath.site/)
expression using the tyranno-defined function `vr_minor`.

```yaml
- uses: astral-sh/setup-uv@v5
  with:
    # :tyranno: python-version: "${{.main-python-version|vr_minor(@)}}"
    python-version: "3.13"
```

If you wanted, you could define `main-python-version` dynamically, too.
Find the max version compatible with `requires-python`:

```toml
[project]
requires-python = ">=3.11,<4.0"

[tool.tyranno.data]
# uses two custom functions that Tyranno provides: vrspec_filter and vr_max
# :tyranno: main-python-version = "${{project.requires-python|vrspec_filter('python',@)|vr_max(@)}}"
main-python-version = "3.13.1"
```

### 🍁 Contributing

New issues and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/tyranno-sandbox/blob/master/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/tyranno-sandbox/blob/main/SECURITY.md).

```text
                    __
                   / _)
        _.----._/ /  _ ,
  .___/        / / = = ,
:----- | ) - ( |
       : :   : :
```

<small>It’s a <s>turtle with arms.</s> <s>dog.</s> <s>misshapen mango?</s> T-rex.</small>
