
name_list = None
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

for name in name_list:
    with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as sample:
        sample_file = sample.read()

    name = name.strip('\n')
    new_txt_file = sample_file.replace("[name]", name)
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_{name}.txt", "w") as new_file:
        new_file.write(new_txt_file)

