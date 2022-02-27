import re, nltk

try:
    nltk.corpus.stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
finally:
    from nltk.corpus import stopwords

try:
    nltk.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
finally:
    from nltk.stem import WordNetLemmatizer


class ProcessTweet:
    """
    Processes tweets to extract the text
    """

    def preprocess(self, text, remove_mention=True, remove_special_char=True):
        """Preprocess the data and return

        Args:
            text (_type_): Input text
            remove_mention (bool, optional): Whether remove mentioned user from tweets. Defaults to True.
            remove_special_char (bool, optional): Whether remove the special character. Defaults to True.

        Returns:
            str: Returns the processed text
        """
        if remove_mention:
            text = self.__remove_mentioned_pattern(text)
        if remove_special_char:
            text = self.__remove_special_character(text)
        text = self.__remove_short_words(text)
        text = self.__remove_stopwords(text)

        return text


    def standardize(self, text, return_type='str'):
        """
        Standardize the tweet text

        Args:
            text (any): Input tweet text
            return_type (str, optional): Return type str or else list. Defaults to 'str'.

        Returns:
            [str|list]: Returns the lemmatized text
        """
        lemmatizer = WordNetLemmatizer()
        lemmatized_text = [lemmatizer.lemmatize(word) for word in text.split()]

        if return_type == 'str':
            return " ".join(lemmatized_text)
        elif return_type == 'list':
            return lemmatized_text
        else:
            raise ValueError("Return type should be str or list")


    def __remove_mentioned_pattern(self, text, pattern = "@[\w]*"):
        """
        Removes the mentioned pattern from the tweet text.
        Defaults patter in `@user` mention in twitter tweets.

        Args:
            text (any): Input to be processed
            pattern (str, optional): Pattern. Defaults to "@[\w]*".
        """        """"""
        return re.sub(pattern, '', text)

    def __remove_special_character(self, text, pattern = "[^a-zA-Z# ]"):
        """
            Remove everything except A-Z, a-z, single # with a space
            after it.

        Args:
            text (any): _description_
            pattern (str, optional): Pattern. Defaults to "[^a-zA-Z# ]".
        """
        return re.sub(pattern, '', text)

    def __remove_short_words(self, text, min_length=3):
        """
            Remove any word with a length less than min_length

        Args:
            text (any): input string
            min_length (int, optional): _description_. Defaults to 3.
        """
        return " ".join([word for word in text.split() if len(word)>=min_length])

    def __remove_stopwords(self, text):
        """
        Remove the stopwords listen in nltk.corpus.stopwords

        Args:
            text (any): Input text
        """
        sw = stopwords.words('english')
        return " ".join([word.lower() for word in text.split() if word.lower() not in sw])


