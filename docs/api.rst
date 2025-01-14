Preprocessing: `pp`
===================
.. module:: dandelion.preprocessing

.. autosummary::
   :toctree: modules

   assign_isotype
   assign_isotypes
   calculate_threshold
   create_germlines
   filter_bcr
   format_fasta
   format_fastas
   quantify_mutations
   reannotate_genes
   reassign_alleles

Preprocessing (external): `pp.external`
=======================================
.. module:: dandelion.preprocessing.external

.. autosummary::
   :toctree: modules

   assigngenes_igblast
   creategermlines
   makedb_igblast
   parsedb_heavy
   parsedb_light
   parsedb_light
   recipe_scanpy_qc
   tigger_genotype

Tools: `tl`
===========
.. module:: dandelion.tools

.. autosummary::
   :toctree: modules

   clone_centrality
   clone_degree
   clone_diversity
   clone_overlap
   clone_rarefaction
   clone_size   
   define_clones
   extract_edge_weights
   find_clones
   generate_network
   transfer

Plotting: `pl`
==============
.. module:: dandelion.plotting

.. autosummary::
   :toctree: modules

   barplot
   clone_network
   clone_overlap
   clone_rarefaction   
   spectratype
   stackedbarplot   

Utilities: `utl`
================
.. module:: dandelion.utilities

.. autosummary::
   :toctree: modules

   Dandelion
   load_data
   makeblastdb   
   read_h5
   read_pkl
   update_metadata
   

Dandelion
=========
.. module:: dandelion.utilities.Dandelion

.. autosummary::
   :toctree: modules

   copy
   update_germline
   write_h5
   write_pkl
   