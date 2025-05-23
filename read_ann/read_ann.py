# Read a Brat ANN file
# "read_ann/MACCROBAT2020/15939911.ann"
def read_file(my_file: str):
    """_summary_

    Args:
        my_file (str): _description_
    """
    with open(my_file, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())  # Print each annotation line