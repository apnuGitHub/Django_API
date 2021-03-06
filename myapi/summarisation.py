# -*- coding: utf-8 -*-
"""summarisation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12DKqriTcg9Pb4eaq-q3tc47bNrqiYzVA
"""


import torch
import transformers
import sys
from transformers import BartTokenizer, BartForConditionalGeneration

torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'

#collapse-show
#long_text=sys.argv[1]
LONG_BORING_TENNIS_ARTICLE='it is different from normal speech w.r.t. to speech production and perception perspective. Recently, authors have proposed Generative Adversarial Network (GAN)-based architecture (namely, DiscoGAN) to discover such cross-domain relationships for whisper-to-normal speech (WHSP2SPCH) con- version. In this paper, we extend this study with detailed theory and analysis. In addition, Cycle-consistent Adversarial Network (CycleGAN) is also proposed for the cross-domain WHSP2SPCH conversion. We observe that the proposed systems yield objective results that are comparable to the baseline, and are superior in terms of fundamental frequency (i.e., F0) prediction. Moreover, we observe that the proposed cross-domain architectures have been preferred 55.75% (on average) times more compared to the traditional GAN in the subjective evaluations. This reveals that the proposed method yields a more natural-sounding normal speech converted from whispered speech.'
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')


def summarise(text):
  article_input_ids = tokenizer.batch_encode_plus([text], return_tensors='pt', max_length=1024)['input_ids'].to(torch_device)
  summary_ids = model.generate(article_input_ids,
                              num_beams=4,
                              length_penalty=2.0,
                              max_length=142,
                              min_length=56,
                              no_repeat_ngram_size=3)

  summary_txt = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)
  return summary_txt
