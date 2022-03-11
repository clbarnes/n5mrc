from pathlib import Path

import mrcfile
import numpy as np
import zarr

from n5mrc.cli import main


def test_importable():
    import n5mrc

    assert n5mrc.__version__


def get_mrc_data(fpath):
    with mrcfile.open(fpath) as f:
        return f.data[:]


def get_n5_data(root, ds):
    store = zarr.N5FSStore(root, mode="r")
    group = zarr.Group(store, read_only=True)
    return group[ds][:]


def assert_n5_eq_mrc(root, ds, mrc_path):
    n5_arr = get_n5_data(root, ds)
    mrc_arr = get_mrc_data(mrc_path)
    assert np.allclose(n5_arr, mrc_arr)


def test_converts(n5_root, dtype, tmpdir):
    mrc_path = str(tmpdir.join(dtype.name + ".mrc"))
    in_ds = dtype.name
    main(n5_root, in_ds, mrc_path)
    assert Path(mrc_path).is_file()
    assert_n5_eq_mrc(n5_root, dtype.name, mrc_path)
