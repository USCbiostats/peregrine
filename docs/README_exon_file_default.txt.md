# Download exon_file_default.txt

Data was downloaded from https://grch37.ensembl.org/biomart/martview/f4c200b649ceea16a7db20ec6e44b8f4. The specific columns to select are shown below:
![image](https://github.com/USCbiostats/peregrine/assets/2678599/e3566ffa-cb18-451c-829b-526e66383ca2)
Click Attributes, select "Structures". Check these fields:
* GENE > Ensembl > Gene stable ID
* GENE > Ensembl > Chromosome/scaffold name
* GENE > Ensembl > Gene name
* GENE > Ensembl > Gene type
* EXON > Exon Information > Exon region start (bp)
* EXON > Exon Information > Exon region end (bp)

Click Results. Ensure "File" and "TSV" are selected in the drop-downs and click Go:
![image](https://github.com/USCbiostats/peregrine/assets/2678599/30ecb305-befb-4245-98e8-45521ed22a36)

This downloaded file was then renamed as exon_file_default.txt.
