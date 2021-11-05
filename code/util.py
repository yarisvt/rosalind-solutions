import re
import requests
from collections import Counter

from Bio import SeqIO

DNA_COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}

RNA_COMPLEMENT = {"A": "U", "U": "A", "G": "C", "C": "G"}

RNA_TO_ONE_PROTEIN = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",

    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",

    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",

    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

CODONS_PER_AMINO_ACID = dict(Counter(RNA_TO_ONE_PROTEIN.values()))

MONOISOTOPIC_MASS_TABLE = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333
}


def get_seq(file: str) -> list[str]:
    seqs = []
    with open(file, "r") as f:
        for line in f:
            seqs.append(line.strip())
    return seqs


def read_fasta_file(file: str) -> list[list[str, str]]:
    fasta_data = []
    with open(file, "r") as f:
        fasta_sequences = SeqIO.parse(f, format="fasta")
        for fasta in fasta_sequences:
            fasta_data.append([fasta.id, str(fasta.seq)])
    return fasta_data
    

def get_fasta_from_uniprot_id(uniprot_id: str) -> None:
    r = requests.get(f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta")
    return r.text


def is_dna(seq: str) -> bool:
    return re.match(r"[^ATGCN]", seq) is None


def is_rna(seq: str) -> bool:
    return re.match(r"[^AUGCN]", seq) is None


def is_protein(seq: str) -> bool:
    return re.match(r"[^ACDEFGHIKLMNPQRSTVWY]", seq) is None
