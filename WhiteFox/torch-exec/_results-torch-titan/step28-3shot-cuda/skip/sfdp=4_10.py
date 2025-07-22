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

    def __init__(self, config):
        super().__init__()
        self.multihead_attention = torch.nn.MultiheadAttention(input_dim, num_heads)

    def forward(self, query, key, value, attn_mask):
        return self.multihead_attention(query, key, value, attn_mask)




config = {'d_model': 3, 'd_k': 3, 'd_v': 3, 'num_heads': 3}

func = Model(config).to('cuda')



query = torch.randn(1, 2, 3)



key = value = torch.randn(1, 3, 3)



vmask = torch.ones(size=(1, 2, 3))

value = 1

test_inputs = [query, key, vmask, value]
