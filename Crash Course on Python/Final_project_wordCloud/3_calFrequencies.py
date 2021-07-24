def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    file_contents = file_contents.lower()
    split_file_contents = file_contents.split()
    word_cloud = {}

    for file_content in split_file_contents:
        word = ""
        for letter in file_content:
            if letter.isalpha():
                word+=letter
        if word not in uninteresting_words:
            i = 0
            for key, value in word_cloud.items():
                if word == key:
                    word_cloud[key] = value+1
                    i += 1
                    break
            if i==0:
                word_cloud[word] = 1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_cloud)
    return cloud.to_array()
