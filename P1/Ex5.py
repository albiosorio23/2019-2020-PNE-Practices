from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
bases = ["A","G", "C", "T"]



print(f"Sequence 1: (Length: {s1.len()}) {s1}")
for b in bases:

    print(b, s1.count_base(b))
print(f"Sequence 1: (Length: {s2.len()}) {s2}")

print(f"Sequence 1: (Length: {s3.len()}) {s3}")

