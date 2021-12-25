#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# My first example with AutoDock Vina in python
#

from vina import Vina


v = Vina(sf_name='vina')

v.set_receptor('3c7q_prot.pdbqt')

v.set_ligand_from_file('ZINC20533791.pdbqt')
v.compute_vina_maps(center=[15.190, 53.903, 16.917], box_size=[25, 25, 25])

# Dock the ligand
v.dock(exhaustiveness=32, n_poses=20)
v.write_poses('ZINC20533791_out.pdbqt', n_poses=5, overwrite=True)
