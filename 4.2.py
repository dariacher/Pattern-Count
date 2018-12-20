import itertools
import sys


def hammingDistance(pat1, pat2):
    hD = 0
    for i in range(len(pat1)):
        if pat1[i] != pat2[i]:
            hD += 1
    return hD


def d(pattern, dna):
    k = len(pattern)
    dist = list(hammingDistance(pattern, dna[i:i + k]) for i in range(len(dna) - k + 1))
    minD = min(dist)
    return minD


def distOfDna(dna, pattern):
    sum = 0
    for dnai in dna:
        sum += d(pattern, dnai)
    return sum


def medianString(dna, k):
    distance = sys.maxsize
    medianStr = ""
    nucleotids = "AGCT"
    patterns = map(''.join, itertools.product(nucleotids, repeat=k))
    for i in patterns:
        if distance > distOfDna(dna, i):
            distance = distOfDna(dna, i)
            medianStr = i

    return medianStr


def main():
    k = int(sys.stdin.readline().rstrip())
    dna = []
    string = sys.stdin.readline()
    while string != "\n" and string != "":
        dna.append(string.rstrip())
        string = sys.stdin.readline()
    print(medianString(dna, k))
main()
