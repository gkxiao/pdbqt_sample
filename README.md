<h2>case study</h2>
<p>The following molecules were used as decoy in VEGFR2 of the DEKOIS 2.0 <sup>[1]</sup> and were used to test MolToPDBQTBlock and MolFromPDBQTBlock function in the <a ref='https://github.com/biocheming/watvina'>watvina/rdkit2pdbqt.py</a><sup>[2]</sup>. </p>
<ol>
<li>ZINC20533791</li>
<img src='https://github.com/gkxiao/pdbqt_sample/blob/main/ZINC20533791.png' alt="ZINC20533791">
<p>ZINC ID: 20533791</p>
<p>SMILES: [H]/N=C1/SC(C(=O)Nc2ccc(C(=O)[O-])cc2)CC(=O)N1/N=C/c1c[nH]c2ccccc12</p>
<li>ZINC22579716</li>
<img src='https://github.com/gkxiao/pdbqt_sample/blob/main/ZINC22579716.png' alt="ZINC22579716">
<p>ZINC ID: 22579716</p>
<p>SMILES: Cc1ccc(C2CC(C(F)(F)F)n3nc(C(=O)N4CC[NH+]5CCCC5C4)c(Cl)c3N2)cc1</p>

<li>ZINC08441965</li>
<img src='https://github.com/gkxiao/pdbqt_sample/blob/main/ZINC08441965.png' alt="ZINC22579716">
<p>ZINC ID: 08441965</p>
<p>SMILES: [H]/N=C1\C(C#N)C2=CC[NH+](Cc3ccccc3)CC2C(c2ccc(OC)c3ccccc23)C1(C#N)C#N</p>
</ol>
<h2>Step to reproduce the results</h2>
<pre line="1" lang="python">
python docking.py
</pre>

<h2>Reference</h2>
<p>(1) Bauer, M. R.; Ibrahim, T. M.; Vogel, S. M.; Boeckler, F. M. Evaluation and Optimization of Virtual Screening Workflows with DEKOIS 2.0 – A Public Library of Challenging Docking Benchmark Sets. J. Chem. Inf. Model. 2013, 53 (6), 1447–1462. https://doi.org/10.1021/ci400115b.</p>
<p>(2)https://github.com/biocheming/watvina</p>
