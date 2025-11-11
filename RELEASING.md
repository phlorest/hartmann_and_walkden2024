# Releasing

Check for any open issues on the repository.

Recreate the CLDF data and make sure it's valid:
```shell
cldfbench makecldf --glottolog-version v5.2 --with-zenodo --with-cldfreadme cldfbench_hartmann_and_walkden2024.py
pytest
```

Recreate the README:
```shell
cldfbench readme cldfbench_hartmann_and_walkden2024.py
```

Run Phlorest-specific checks on the data:
```shell
phlorest check --with-R cldfbench_hartmann_and_walkden2024.py
```

Check whether new files have been generated (and add them if so):
```shell
git status
```

Figure out the new release tag:
```shell
git tag
```

Commit and push the release-ready data:
```shell
git commit -a -m"release vX.Y"
git push origin
```

Create the release instruction:
```shell
phlorest release cldfbench_hartmann_and_walkden2024.py vX.Y
```

Make sure the repository is wired up with Zenodo, and if so run the `gh release` command as
given in the output of `phlorest release`.
