with open('dna.txt', 'r') as f:
    header = next(f).replace("\n","")
    for character in user_input:
        if character == "A":
            sum_A = sum_A + 1
        elif character == "C":
            sum_C = sum_C + 1
        elif character == "T":
            sum_T += 1
        elif character == "G":
            sum_G += 1
        total_length += 1

print ("The total lenght is:", total_length, "\nA:", sum_A,"\nC:", sum_C, "\nT:", sum_T,"\nG:", sum_G)
