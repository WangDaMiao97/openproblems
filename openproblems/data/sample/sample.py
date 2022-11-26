from ..utils import loader

import anndata
import numpy as np
import pandas as pd
import pathlib
import scipy.sparse

SCRIPT_PATH = pathlib.Path(__file__)


@loader(
    data_url="https://openproblems.bio",
    data_reference="https://github.com/openproblems-bio/openproblems",
)
def load_sample_data(test=True):
    """Create a simple dataset to use for testing in multimodal applications.

    Genes and cells generated by:
    ```
    from ..multimodal.scicar.cell_lines import rna_cells_url
    from ..multimodal.scicar.cell_lines import rna_genes_url
    genes = pd.read_csv(rna_genes_url, low_memory=False, index_col=0, nrows=500)
    cells = pd.read_csv(rna_cells_url, low_memory=False, index_col=0, nrows=200)
    ```
    """
    assert test

    genes = pd.read_csv(
        SCRIPT_PATH.parent.joinpath("sample_genes.csv.gz"),
        low_memory=False,
        index_col=0,
    )
    cells = pd.read_csv(
        SCRIPT_PATH.parent.joinpath("sample_cells.csv.gz"),
        low_memory=False,
        index_col=0,
    )

    rna_data = scipy.sparse.csr_matrix(
        np.random.poisson(0.3, (cells.shape[0], genes.shape[0])).astype(np.float32)
    )

    adata = anndata.AnnData(rna_data, obs=cells, var=genes)
    return adata