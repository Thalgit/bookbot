def word_counter(input_path):
        try:
            with open(input_path) as f:
                return len(f.read().split())
        except FileNotFoundError:
            print(f"File not found: {input_path}")
            return 0
        
def character_counter(input_path):
    with open(input_path) as f:
        char_dict = {}
        text = f.read().lower()
        for i in text:
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
    return char_dict

def character_sorter(char_dict):
    pairs = []
    for ch, count in char_dict.items():
        pairs.append({"char": ch, "num": count})
    def sort_on(item):
        return item["num"]
    pairs.sort(reverse=True, key=sort_on)
    return pairs