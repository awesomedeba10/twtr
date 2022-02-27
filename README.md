# TWTR

twtr is package use to process and lemmatized the text data as part of NLP. Done under the AlmaBetter Assignment to process Twitter data and make this ready for modeling.

## Installation

Install Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
from twtr.ProcessTweet import ProcessTweet

tweet = ProcessTweet()

print(tweet.preprocess("I love Lionel Messi and his jersey no. was 10 at @fcbarcelona")
# prints love lionel messi his jersey

print(tweet.standardize('love lionel messi his jersey', return_type='list'))
# prints ['love', 'lionel', 'messi', 'his', 'jersey']
```

## License
[MIT]()