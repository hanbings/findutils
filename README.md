# findutils

[![Crates.io](https://img.shields.io/crates/v/findutils.svg)](https://crates.io/crates/findutils)
[![Build status](https://ci.appveyor.com/api/projects/status/wrmbs03dn6sb721e/branch/master?svg=true)](https://ci.appveyor.com/project/Arcterus/findutils/branch/master)
[![codecov](https://codecov.io/gh/uutils/findutils/branch/master/graph/badge.svg)](https://codecov.io/gh/uutils/findutils)

Rust implementation of [GNU findutils](https://www.gnu.org/software/findutils/).

## Run the GNU testsuite on rust/findutils:

```
bash util/build-gnu.sh

# To run a specific test:
bash util/build-gnu.sh tests/misc/help-version.sh
```