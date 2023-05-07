# Releases

## Overview

Releases on this project are triggered through GitHub Actions listening for differences between our `main` and `develop` branches. A pull request for the next release is created by a github-actions bot and merging this pull request automatically delivers the changes up to production.

## Creating a release

A release pull request (PR) is created anytime something new is merged to `develop` that has not yet been merged to `main`. To execute a release and kickoff the CI process: 
- Find the automated PR that was created by github-actions.
  - It will always have a "Release: v#.#.#" title.
- Copy the list from the "changelog" comment
- Edit the description of the release PR
- Paste in the list of changes and distribute each item accordingly to the Improvements and Technical sections
- Update `CHANGELOG.md` as part of the release PR:
  - Copy the whole "Unreleased" section and paste above it
  - Replace the lower "Unreleased" title with the version in the release PR
  - In the top unreleased section remove all references from each of the five lists (reset it to be blank)
  - In the section covering this release's changes, remove any of the sections that have no PRs referenced (e.g. if "Removed" has no PRs in it, you can remove that section title)
  - At the very bottom there is a list of the versions.
    - Copy the top version list line and paste it at the top of the same list
    - Change the numbers to now reflect this change
- Merge the PR to main
- This will kick off a continuous 

### Note

Once more PRs are merged to `develop` a new Release PR will be created automatically. We will never have to write a release PR from scratch.

## Updating the CHANGELOG.md

Besides the [version changelog](https://github.com/CodeForPhilly/third-places/releases) that is automatically created as releases are executed, we also keep a [CHANGELOG.md](https://github.com/CodeForPhilly/third-places/blob/develop/CHANGELOG.md) that is updated with each pull request that is merged to develop to help keep track of what changes are made.

The changelog itself links to [documentation](https://keepachangelog.com/en/1.0.0/) describing the format. The essential form is a list of PR titles and links to those PRs organized by what release they go with and what category of change they are making.
