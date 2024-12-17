"""
File:    twitters_ats.py
Author:  Mathew Dawit
Date:    10/10/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
  The program extracts unique Twitter usernames (after @) and
  hashtags (after #) from a tweet and returns them in two separate
  lists.
"""


def twitter_ats(the_tweet):
    """
    A function to find the ats and tags in a twitter tweet
    :param the_tweet: the phrase to separate into ats and tags
    :return: two different lists contained the ats and the tags in the original tweet
    """

    tweet_split = the_tweet.split()
    at_list = []
    at_list_no_at = []
    tag_list = []
    tag_list_no_tag = []

    for tweets in tweet_split:
        if '@' in tweets and tweets not in at_list and '@#' not in tweets:
            at_list.append(tweets)
            at_list_no_at.append(tweets.strip('@'))

        elif '#' in tweets and '#@' not in tweets and '@#' not in tweets:
            tag_list.append(tweets)
            tag_list_no_tag.append(tweets.strip('#'))
            
    return at_list_no_at, tag_list_no_tag


if __name__ == '__main__':
    the_tweet = input("What do you want to tweet? ")

    if '#' in the_tweet or '@' in the_tweet:  
        split_tweet = twitter_ats(the_tweet)
        print("The users were:", ", ".join(split_tweet[0]))
        print("The hash-tags are:", ", ".join(split_tweet[1]))
