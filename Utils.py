dataset_folder = "dataset/"
results_folder = "results/"


def text4csv(text):
    text = str(text)
    text = text.replace(";"," ")
    text = text.replace("\n"," ")
    return text