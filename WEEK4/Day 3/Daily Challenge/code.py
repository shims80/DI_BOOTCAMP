# Daily challenge week 04 day 03
# Week04 Day03 - Daily Challenge - Caesar Cypher

sample_txt = "abcde fghij klmn opqr stuvw xyz"


def is_alpha(str):
    for l in str:
        code = ord(l)
        if not(64 < code < 91 or 96 < code < 123):
            return False
    return True


def main():
    while True:
        input_action = input("C for Cypher / D for Decypher / S for Stop : ")
        if input_action in ["S", "s"]:
            break
        if input_action in ["D", "d"]:
            cypher = -1
        elif input_action in ["C", "c"]:
            cypher = 1
        else:
            continue
        cypher_text = ""
        input_txt = input(
            "Enter a text, please (empty string stops the program): ")
        if input_txt == "":
            break
        for letter in input_txt:
            if is_alpha(letter):
                if cypher == 1 and ((ord(letter) > 119) or (87 < ord(letter) < 91)):
                    cypher_text += chr(ord(letter) - 23)
                elif cypher == -1 and ((ord(letter) < 68) or (96 < ord(letter) < 100)):
                    cypher_text += chr(ord(letter) + 23)
                else:
                    cypher_text += chr(ord(letter) + 3 * cypher)
            else:
                cypher_text += letter
        print("\n" + input_txt + "\n" + cypher_text + "\n")


if __name__ == "__main__":
    main()
