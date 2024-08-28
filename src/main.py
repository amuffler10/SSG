from textnode import TextNode
from htmlnode import *

def main():
    node_a = LeafNode("p", "This is a paragraph of text.")
    node_b = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    
    print(node_a.to_html())
    print("-------------------")
    print(node_b.to_html())

main()

