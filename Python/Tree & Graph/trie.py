#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# * trie, prefix tree


class Node:
    def __init__(self):
        self.word = None
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.word = word

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False, None
            node = node.children[c]
        return True, node.word

    @staticmethod
    def __collect_words(node):
        results = []
        if node.word:
            results.append(node.word)
        for k, v in node.children.items():
            results.extend(Trie.__collect_words(v))
        return results

    def auto_complete(self, prefix_word):
        node = self.root
        for c in prefix_word:
            if c not in node.children:
                return []
            node = node.children[c]
        return self.__collect_words(node)
    

