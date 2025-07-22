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

class MultiHeadAttention(torch.nn.Module):

    def __init__(self, attention_dim, n_heads):
        super().__init__()
        self.fc_q = torch.nn.Linear(attention_dim, attention_dim)
        self.fc_k = torch.nn.Linear(attention_dim, attention_dim)
        self.fc_v = torch.nn.Linear(attention_dim, attention_dim)
        self.attention_layers = torch.nn.ModuleList([nn.Sequential(nn.Linear(64, 32), nn.Tanh(), nn.Linear(32, 8), nn.Tanh(), nn.Linear(8, 1)) for _ in range(n_heads)])

    def forward(self, query, key, value, dropout_p):
        (b, n, s) = query.shape
        d = s // n
        r = d // s
        q = self.fc_q(query)
        k = self.fc_k(key)
        v = self.fc_v(value)
        q = self.attention_layers(q)
        k = self.attention_layers(k)
        v = self.attention_layers(v)
        q = q.reshape(b, 16, 32)
        return q * k * (v * (1 / r))

class Model(torch.nn.Module):

    def __init__(self, attention_dim=64):
        super().__init__()
        self.attention_layers = torch.nn.ModuleList([MultiHeadAttention(attention_dim, 8) for _ in range(8)])

    def forward(self, x1, x2, w1, w2, dropout_p):
        x3 = torch.cat((x1, x2), dim=1)
        for layer in self.attention_layers:
            x3 = layer(x3, x3, x3, dropout_p)
        return x3


func = Model().to('cpu')


x1 = torch.randn(1, 16, 64)

x2 = torch.randn(1, 16, 64)

w1 = torch.randn(1, 16, 64)

w2 = torch.randn(1, 16, 64)
dropout_p = 1

test_inputs = [x1, x2, w1, w2, dropout_p]

# JIT_FAIL
'''
direct:
Module [ModuleList] is missing the required "forward" function

jit:
Module [ModuleList] is missing the required "forward" function
'''