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

    def __init__(self, qkv_input_dim, seq_length, num_heads, head_dim, dropout_p=0.2):
        super().__init__()
        attention = torch.nn.Linear(qkv_input_dim, ((seq_length * num_heads) * head_dim), bias=True)
        self.attention = MultiheadAttentionLayer(attention, seq_length, num_heads, head_dim, dropout_p=dropout_p)

    def forward(self, query, key, value):
        return self.attention(query, key, value)



qkv_input_dim = 1
seq_length = 1
num_heads = 1
head_dim = 1

func = Model(qkv_input_dim, seq_length, num_heads, head_dim).to('cuda')

query = 1
key = 1
value = 1

test_inputs = [query, key, value]
