#!/usr/bin/env python
# basic requirements for test data
import sys
import os
import dandelion as ddl
import scanpy as sc
import pandas as pd
import requests
from io import StringIO
from numba.core.errors import (
    NumbaWarning,
    NumbaDeprecationWarning,
    NumbaPendingDeprecationWarning,
)
import warnings

warnings.simplefilter("ignore", category=NumbaWarning)
warnings.simplefilter("ignore", category=NumbaDeprecationWarning)
warnings.simplefilter("ignore", category=NumbaPendingDeprecationWarning)


def test_setup_preprocessing():
    file1 = "https://cf.10xgenomics.com/samples/cell-vdj/5.0.0/sc5p_v2_hs_B_1k_multi_5gex_b/sc5p_v2_hs_B_1k_multi_5gex_b_vdj_b_filtered_contig.fasta"
    file2 = "https://cf.10xgenomics.com/samples/cell-vdj/5.0.0/sc5p_v2_hs_B_1k_multi_5gex_b/sc5p_v2_hs_B_1k_multi_5gex_b_vdj_b_filtered_contig_annotations.csv"
    r1 = requests.get(file1)
    open("test/filtered_contig.fasta", "wb").write(r1.content)
    r2 = requests.get(file2)
    open("test/filtered_contig_annotations.csv", "wb").write(r1.content)


def test_format_headers():
    samples = ["test"]
    ddl.pp.format_fastas(samples, prefix="test")


def test_reannotate():
    samples = ["test"]
    ddl.pp.reannotate_genes(samples)


def test_reassign():
    samples = ["test"]
    ddl.pp.reassign_alleles(samples, combined_folder="test")


def test_assign_isotype():
    samples = ["test"]
    ddl.pp.assign_isotypes(samples, plot=False)


def test_quantify_mut():
    filePath = "test/dandelion/data/test_filtered_contig_igblast_db-pass_genotyped.tsv"
    ddl.pp.quantify_mutations(filePath)


def test_scanpy():
    scfile = "https://cf.10xgenomics.com/samples/cell-vdj/5.0.0/sc5p_v2_hs_B_1k_multi_5gex_b/sc5p_v2_hs_B_1k_multi_5gex_b_count_filtered_feature_bc_matrix.h5"
    r = requests.get(scfile)
    open("test/sctest2.h5", "wb").write(r.content)
    adata = sc.read_10x_h5("test/sctest2.h5")
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
    adata = adata[:, adata.var["highly_variable"]].copy()
    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata, svd_solver="arpack")
    sc.pp.neighbors(adata)
    adata.write("test/sctest2.h5ad", compression="gzip")
    print(adata)


def test_filter():
    adata = sc.read_10x_h5("test/sctest2.h5")
    bcr = pd.read_csv(
        "test/dandelion/data/test_filtered_contig_igblast_db-pass_genotyped.tsv",
        sep="\t",
    )
    bcr.reset_index(inplace=True, drop=True)
    adata.obs["filter_rna"] = False
    vdj, adata = ddl.pp.filter_bcr(bcr, adata)
    adata.write("test/sctest2.h5ad", compression="gzip")
    vdj.write_h5("test/test2.h5", compression="bzip2")


def test_update_metadata():
    test = ddl.read_h5("test/test2.h5")
    ddl.update_metadata(test, "sequence_id")


def test_find_clones():
    test = ddl.read_h5("test/test2.h5")
    ddl.tl.find_clones(test)


def test_generate_network():
    test = ddl.read_h5("test/test2.h5")
    ddl.tl.generate_network(test)


def test_downsampling():
    test = ddl.read_h5("test/test2.h5")
    ddl.tl.generate_network(test)
    test_downsample = ddl.tl.generate_network(test, downsample=100)
    print(test_downsample)


def test_transfer():
    test = ddl.read_h5("test/test2.h5")
    adata = sc.read_h5ad("test/sctest2.h5ad")
    ddl.tl.transfer(adata, test)
    adata.write("test/sctest2.h5ad", compression="gzip")


if __name__ == "__main__":
    test_setup_preprocessing()
    test_format_headers()
    test_reannotate()
    test_reassign()
    test_assign_isotype()
    test_quantify_mut()
    test_scanpy()
    test_filter()
    test_update_metadata()
    test_find_clones()
    test_generate_network()
    test_downsampling()
    test_transfer()