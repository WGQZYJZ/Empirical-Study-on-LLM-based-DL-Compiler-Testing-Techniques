import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        embedding_dim = 32
        heads = 2
        dropout_rate = 0.1
        attention_head_dim = int(embedding_dim / heads)
        self.attention_head_dim = attention_head_dim
        self.self_attention = MultiHeadedSelfAttention(embedding_dim=embedding_dim, num_heads=heads)
        self.ffn = FFN(embedding_dim=embedding_dim, hidden_dim=embedding_dim * 2)
        self.layernorm1 = torch.nn.LayerNorm(normalized_shape=embedding_dim, eps=1e-12)
        self.layernorm2 = torch.nn.LayerNorm(normalized_shape=embedding_dim, eps=1e-12)
        self.dropout1 = torch.nn.Dropout(dropout_rate)
        self.dropout2 = torch.nn.Dropout(dropout_rate)

    def forward(self, x, attention_mask=None):
        output = self.layernorm1(x)
        output = self.self_attention(query=output, attention_mask=attention_mask)
        output = self.dropout1(output)
        x = x + output
        output = self.layernorm2(x)
        output = self.ffn(output)
        output = self.dropout2(output)
        x = x + output
        return x


func = Model().to('cuda')


D = 32
N = 32
query = torch.randn(N, D)

D = 32
N = 32
key = torch.randn(N, D)
N = 32
N = 32

attention_mask = torch.randint(low=0, high=2, size=[N, N])

test_inputs = [query, key, attention_mask]
