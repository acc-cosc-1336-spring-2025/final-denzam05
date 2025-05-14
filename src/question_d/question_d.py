#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_most_likely_ancestor_consensus (dna_string1, dna_string2):       

    positions = []

    for i in range (len (dna_string1) - len(dna_string2) + 1):
        if dna_string1 [i:i + len(dna_string2)] == dna_string2:
            positions.append (i + 1)

    return tuple (positions)


def validate_dna_string1 (dna):
    if len(dna) > 8 and len(dna) <= 16:
        return True
    else:
        return False

def validate_dna_string2 (dna):
    if len(dna) == 4:
        return True
    else:
        return False