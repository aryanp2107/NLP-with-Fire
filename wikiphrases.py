#!/usr/bin/env python
import fire
import hello
from nlplogic.corenlp import get_phrases



if __name__ == '__main__':
  fire.Fire(get_phrases)