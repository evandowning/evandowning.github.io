Title: Markov Text Generator
Date: 2016-01-16

For fun, I've recently created my own [Markov](https://en.wikipedia.org/wiki/Markov_chain) text generator.

## Explanation

A Markov text generator takes a piece of text as input and outputs new text that is seemingly random. It may even make syntactical and/or semantic sense if properly seeded with input text.

It accomplishes this by splitting the inputted text into tokens based on some separation character. This can result in individual characters or sequences of characters (recognized as words if the separation character is a space).

It then creates a chain of these tokens based on the order of their appearance in the text. The length of this chain is chosen by the generator's user. It then adds the token appearing immediately after this chain of tokens to a list that is associated with that particular chain of tokens. Repeating this process for all inputted text creates the Markov chain.

To generate the random text, the program chooses a chain of tokens as the starting point of the output text.

It then chooses a random token from the list of tokens associated with the chain and add that token to the output text.

After, it extends the chain of tokens to include this next token while removing the first token from the chain. This creates a new chain of tokens to then choose another random token from the list associated with the chain.

After some determined stopping point, the generator ceases to create more text.

## Example

So, let's say I have the input text "I like bananas and apples and oranges."

Let's say I want to split this text by spaces, isolating the words and character(s) that come immediately after the word.

I also want the chain's length (chain-size from 'Features' above) to be 1.

So the following chain would be created with its associated next tokens:

chain of tokens: list of tokens coming after the chain in the text

```
"I": ["like"]
"like": ["bananas"]
"bananas": ["and"]
"and": ["apples", "oranges."]
"apples": ["and"]
As you can see, the chain "and" has two different words it sees after it in the sentence.
```

So, there's a 50% probability that "apples" or "oranges." will come after the word "and" according to this sentence. However, with the other words there is a 100% probability that the next word will be the only one contained in their list.

You can imagine how more text and chains with lengths greater than 1 will lead to more random and original sentences.

Suppose we don't have any separation. Doing this by character makes it more interesting. It will generate more random words, some misspelled because of the random aspects of chain, and will make less semantic sense than creating chains via words (characters separated by a space).

Here is a link to it: [https://github.com/evandowning/markov-text-generator](https://github.com/evandowning/markov-text-generator)
