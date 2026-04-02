import wikipedia
wikipedia.search("Geolden State Warriors")
[]
wikipedia.search("Golden State Warriors")
['Golden State Warriors',
 '2025–26 Golden State Warriors season',
 '2024–25 Golden State Warriors season',
 '2015–16 Golden State Warriors season',
 'History of the Golden State Warriors',
 'Golden State Warriors draft history',
 '2020–21 Golden State Warriors season',
 '2021–22 Golden State Warriors season',
 '2016–17 Golden State Warriors season',
 'List of Golden State Warriors seasons']
wikipedia.summary("Golden State Warriors")
wikipedia.summary('2025–26 Golden State Warriors season')
'The 2025–26 Golden State Warriors season is the 80th season of the franchise in the National Basketball Association (NBA), their 64th in the San Francisco Bay Area, and their seventh season at the Chase Center.\nWith their loss against the New York Knicks on March 15, the Warriors failed to improve on their 48–34 record from the previous season. On March 29, the Warriors clinched a play-in spot.'
golden_state_warriors_text =  wikipedia.summary('2025–26 Golden State Warriors season')
from textblob import TextBlob
blob = TextBlob(golden_state_warriors_text)
blob.sentiment
Sentiment(polarity=-0.06606060606060607, subjectivity=0.30424242424242426)
blob.tags
[('The', 'DT'),
 ('2025', 'CD'),
 ('26', 'CD'),
 ('Golden', 'NNP'),
 ('State', 'NNP'),
 ('Warriors', 'NNP'),
 ('season', 'NN'),
 ('is', 'VBZ'),
 ('the', 'DT'),
 ('80th', 'JJ'),
 ('season', 'NN'),
 ('of', 'IN'),
 ('the', 'DT'),
 ('franchise', 'NN'),
 ('in', 'IN'),
 ('the', 'DT'),
 ('National', 'NNP'),
 ('Basketball', 'NNP'),
 ('Association', 'NNP'),
 ('NBA', 'NNP'),
 ('their', 'PRP$'),
 ('64th', 'CD'),
 ('in', 'IN'),
 ('the', 'DT'),
 ('San', 'NNP'),
 ('Francisco', 'NNP'),
 ('Bay', 'NNP'),
 ('Area', 'NNP'),
 ('and', 'CC'),
 ('their', 'PRP$'),
 ('seventh', 'JJ'),
 ('season', 'NN'),
 ('at', 'IN'),
 ('the', 'DT'),
 ('Chase', 'NNP'),
 ('Center', 'NNP'),
 ('With', 'IN'),
 ('their', 'PRP$'),
 ('loss', 'NN'),
 ('against', 'IN'),
 ('the', 'DT'),
 ('New', 'NNP'),
 ('York', 'NNP'),
 ('Knicks', 'NNP'),
 ('on', 'IN'),
 ('March', 'NNP'),
 ('15', 'CD'),
 ('the', 'DT'),
 ('Warriors', 'NNS'),
 ('failed', 'VBD'),
 ('to', 'TO'),
 ('improve', 'VB'),
 ('on', 'IN'),
 ('their', 'PRP$'),
 ('48', 'CD'),
 ('34', 'CD'),
 ('record', 'NN'),
 ('from', 'IN'),
 ('the', 'DT'),
 ('previous', 'JJ'),
 ('season', 'NN'),
 ('On', 'IN'),
 ('March', 'NNP'),
 ('29', 'CD'),
 ('the', 'DT'),
 ('Warriors', 'NNS'),
 ('clinched', 'VBD'),
 ('a', 'DT'),
 ('play-in', 'JJ'),
 ('spot', 'NN')]
blob.noun_phrases
WordList(['golden state', 'warriors', '80th season', 'national basketball association', 'nba', 'san francisco', 'bay area', 'chase', 'york knicks', 'march', 'warriors', 'previous season', 'march', 'warriors', 'play-in spot'])
blob.noun_phrases[0]
'golden state'
%history -f ~/my_session.py
!ls ~/my_session.py
%history -f /workspaces/NLP-with-Fire/my_session.py
%history -o -f /workspaces/NLP-with-Fire/my_session.py
