import tweepy
import csv
import zibi_tweets

def tweets_to_csv(screen_name):
    #autoryzacja danych z Twittera
    auth = zibi_tweets.twitter_auth()

    #inicjalizacja tweepy
    api = tweepy.API(auth)

    #pusta lista do zbierania tweetów
    all_tweets = []

    #ostatnie tweety, wykorzystując user_timeline możemy ściągnąć ostatnie 200 tweetów
    last_tweets = api.user_timeline(screen_name = screen_name, count=200)

    # zapisujemy ostatnie tweety
    all_tweets.extend(last_tweets)

    # zapisujemy id najstarszego tweeta - 1
    oldest = all_tweets[-1].id - 1

    # pętla zapisujące tweety aż do wyczerpania twweetów
    while len(last_tweets) > 0:
        print(f"Zapisuje tweet {oldest}")

        # używamy parametru max_id, aby zapobiec duplikatom
        last_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # zapisujemy nowe tweety
        all_tweets.extend(last_tweets)

        # aktualizujemy id najstarszego tweeta - 1
        oldest = all_tweets[-1].id - 1

        print(f"Zapisano dotychczas {len(all_tweets)} tweetów")

    # zapisujemy listę tweetów do 2 wymiarowej matrycy
    output_tweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in all_tweets]

    # zapis do pliku csv
    with open(f'new_{screen_name}_tweets.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(output_tweets)

if __name__ == '__main__':
	#Konto Zbigniewa Bońka: 'BoniekZibi'
	tweets_to_csv("BoniekZibi")









