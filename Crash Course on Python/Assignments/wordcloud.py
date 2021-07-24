names = "Hey, there! Hey are you? Fine men. hey @you? a [beautiful] day is not it"
names = names.lower()
split_names = names.split()

ugly = ['are', 'a', 'is', 'it']

word_cloud = {}

for name in split_names:
        word = ""
        for letter in name:
            if letter.isalpha():
                word+=letter
        if word not in ugly:
            i = 0
            for key, value in word_cloud.items():
                if word == key:
                    word_cloud[key] = value+1
                    i += 1
                    break
            if i==0:
                word_cloud[word] = 1
print(word_cloud)
