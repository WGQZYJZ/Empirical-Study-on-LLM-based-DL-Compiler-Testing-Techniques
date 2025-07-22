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

    def __init__(self, embed_dim, num_heads, dropout_p):
        super().__init__()
        self.head = SingleHeadAttention(embed_dim, num_heads, dropout_p)
        self.layernorm = torch.nn.LayerNorm([embed_dim])

    def forward(self, query, key, value):
        output = self.head(query, key, value)
        output = self.layernorm(output)
        return output


embed_dim = 1
num_heads = 1
dropout_p = 1

func = Model(embed_dim, num_heads, dropout_p).to('cpu')


query = torch.randn(2, 3, 128)

key = torch.randn(2, 4, 128)

value = torch.randn(2, 4, 128)

test_inputs = [query, key, value]
