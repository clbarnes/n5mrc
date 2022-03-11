import numpy as np
import pytest
import zarr
from mrcfile.utils import dtype_from_mode

SEED = 1991
MODES = [
    0,
    1,
    2,
    # 4,  # complex64
    6,
]
DTYPES = [dtype_from_mode(m) for m in MODES]


def random_of_dtype(dtype: np.dtype, shape):
    rng = np.random.default_rng(SEED)
    if np.issubdtype(dtype, np.integer):
        info = np.iinfo(dtype)
        return rng.integers(info.min, info.max, shape, dtype)

    data = rng.random(shape)
    if np.issubdtype(dtype, np.complexfloating):
        comp = rng.random(shape) * 1j
        data = data.astype(comp.dtype) + comp
    return data.astype(dtype)


@pytest.fixture(scope="session")
def n5_root(tmpdir_factory):
    root_path = str(tmpdir_factory.mktemp("root.n5"))
    store = zarr.N5FSStore(root_path)
    group = zarr.Group(store)
    shape = (10, 10, 10)
    chunks = (5, 5, 5)
    for dtype in DTYPES:
        data = random_of_dtype(dtype, shape)
        group.create_dataset(dtype.name, data=data, chunks=chunks)

    return root_path


@pytest.fixture(params=DTYPES)
def dtype(request):
    return request.param
