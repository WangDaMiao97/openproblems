import numpy as np


def check_dataset(adata):
    assert "mode2" in adata.obsm
    assert "mode2_obs" in adata.uns
    assert "mode2_var" in adata.uns
    assert "mode2_var_chr" in adata.uns
    assert "mode2_var_start" in adata.uns
    assert "mode2_var_end" in adata.uns
    return True


def check_method(adata):
    assert "gene_score" in adata.obsm
    return True
