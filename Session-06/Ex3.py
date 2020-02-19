class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        #print("New sequence created! ")


    def __str__(self):
        return self.strbases


    def len(self):
        return len(self.strbases)



def print_seqs(seq_list):
    for seq in seq_list:
        print(f"Sequence {seq_list.index(seq)}: (Length: {seq.len()}) {seq}")




def generate_seqs(pattern, number):
    new_seq = []
    for element in range (1, number +1): #Para que vaya del 1 al 3 y del 1 al 5
        new_seq.append(Seq(pattern * element)) #llamas a la class seq, Multiplicas la letra que quieres por el numero de veces
    return new_seq

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print()
print("List 1:")
print_seqs(seq_list1)

print ()
print("List 2:")
print_seqs(seq_list2)
