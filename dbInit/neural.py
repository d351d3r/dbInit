from dostoevsky.models import FastTextSocialNetworkModel
from dostoevsky.tokenization import RegexTokenizer

from alg import formula_fedosa
from web_parse import parse_web_irec

def predict(textsLists):
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    results = model.predict(textsLists, k=5)

    marks = []
    for res in results:
        positive = res['positive']
        neutral = res['neutral']
        negative = res['negative']
        marks.append(formula_fedosa(positive, neutral,negative))
    
    return marks

