from pathlib import Path

import mrcfile
import numpy as np
import pytest
import zarr

from n5mrc.cli import main, parse_subvolume


def test_importable():
    import n5mrc

    assert n5mrc.__version__


def get_mrc_data(fpath):
    with mrcfile.open(fpath) as f:
        return f.data[:]


def get_n5_data(root, ds, sub=None):
    if sub is None:
        sub = (slice(None),)
    store = zarr.N5FSStore(root, mode="r")
    group = zarr.Group(store, read_only=True)
    return group[ds][sub]


def assert_mrc_eq_n5(mrc_path, root, ds, sub=None):
    n5_arr = get_n5_data(root, ds, sub=sub)
    mrc_arr = get_mrc_data(mrc_path)
    assert np.allclose(n5_arr, mrc_arr)


@pytest.mark.parametrize("sub", [None, (slice(2, 8),)*3])
def test_converts(n5_root, dtype, tmpdir, sub):
    mrc_path = str(tmpdir.join(dtype.name + ".mrc"))
    in_ds = dtype.name
    main(n5_root, in_ds, mrc_path, sub)
    assert Path(mrc_path).is_file()
    assert_mrc_eq_n5(mrc_path, n5_root, dtype.name, sub)


@pytest.mark.parametrize(["to_parse", "expected"], [
    ("10:100", (slice(10, 100),)),
    (":100", (slice(None, 100),)),
    ("10:", (slice(10, None),)),
    ("10", (10,))
])
def test_parse_sub(to_parse, expected):
    parsed = parse_subvolume(to_parse)
    assert parsed == expected
