#!/usr/bin/env python3

import requests
import random

r = requests.get('https://cat-fact.herokuapp.com/facts')

def highest_upvotes():
        upvote_list = []
        for x in r.json()["all"]:
            upvote_list.append(x.get("upvotes"))
        print("\nThe highest upvote count was:")
        print("=============================")
        print(max(upvote_list))


def name_calling():
    name_list = []
    for name in r.json()["all"]:
        if name.get("user"):
            name_list.append(f'{name["user"]["name"]["first"]} {name["user"]["name"]["last"]} is a dumb name.')
    for x in name_list:
        print(x)

def random_cat_fact():
    fact_list= []
    for x in r.json()["all"]:
        fact_list.append(x.get("text"))
    list_count= len(fact_list) - 1
    random_fact= random.randint(0, list_count)
    print("\nEnjoy a random cat fact!")
    print("========================")
    print(fact_list[random_fact])

highest_upvotes()
name_calling()
random_cat_fact()
