import random

countries = ['algeria', 'angola', 'benin', 'sudan']
numcountries = len(countries)
score = 0
print('Number of Countries to Guess: {0}'.format(len(countries)))
print('Current Score: {0}'.format(score))

country_img_dic = {'algeria': 'alg.png', 'angola': 'angola.png', 'benin': 'benin.png'}

next_country = random.sample(countries, 1)
nxt_cnt_str = ''.join(str(c) for c in next_country)

def display_country(next_country):
    # display picture of country on map

    nxt_img = country_img_dic[nxt_cnt_str]
    print('picture of {0}'.format(''.join(nxt_cnt_str)))




def user_input():
    print('Enter Guess')
    user_guess = 'benin'


if user_guess == next_country:
    print('great guess!')
    score +=1
    countries.remove(nxt_cnt_str)


display_country(next_country)
user_input()-+