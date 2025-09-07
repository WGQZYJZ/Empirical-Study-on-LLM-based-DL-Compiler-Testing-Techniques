

import torch 
from torch import nn
 
class Model(nn.Module):
    def __init__(self, embedding_dim=768, vocab_size = 1024):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)

    def forward(self, input):
       return self.embedding(input).sum()

