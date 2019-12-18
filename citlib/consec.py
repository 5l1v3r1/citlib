import os
import sys

def get_letters(t):
    letters = []
    for i in range(t):
        letter = str(chr(i+65))
        letters.append(letter)
    return letters

def generate(t=3):
    dirname, _ = os.path.split(os.path.abspath(__file__))
    file = dirname + "/../generated/" + "consec" + str(t) + ".lp"
    print("Generating " + file + " as requested from the user...")
    letters = get_letters(t)
    content = "consec(" + ",".join(letters) + ") :- "
    order = "order(" + ",".join(letters) + ")."
    edge = ""
    not_flows = []
    for i in range(t-1):
        letter = str(chr(i+65))
        next_letter = str(chr(i+66))
        edge += "edge(" + letter + "," + next_letter + ")"
        not_flow = ":- not flow(" + letter + "," + next_letter + ",1), " + order
        not_flows.append(not_flow)
        if i == t-2:
            edge += "."
        else:
            edge += ", "
    content += edge + "\n" + "\n".join(not_flows)
    # Write to file
    f = open(file, "w")
    f.write(content)
    f.close()

if __name__ == "__main__":
    # Arg is order
    generate(sys.argv[0])