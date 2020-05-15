'''
Code By:Rushikesh Patil
This is small python programm to search the sentences you need in short a 'mini search engine'
'''
def searcheng(sentence1,sentence2):
    words1=sentence1.split(' ')
    words2=sentence2.split(' ')
    score=0
    for word1 in words1:
        for word2 in words2:
            if word1.lower()==word2.lower():
                score+=1
    return score
if __name__ == "__main__":
    sentences=['python contains lists','python has tupels','python has dictionaries','python contains sets']
    search=input('search the sentence ')
    scores=[searcheng(search,sentence) for sentence in sentences]
    sortedscore=[sortedsent for sortedsent in sorted(zip(scores, sentences), reverse=True)]
    # print(sortedscore)                
    print(f'{len(sortedscore)} results are found:')
    for score,item in sortedscore:
        print(f'  "{item}" with a score of {score}')