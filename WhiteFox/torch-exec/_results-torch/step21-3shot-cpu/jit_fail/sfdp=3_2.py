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

    def __init__(self, attention_dim, batch_size=16, num_heads=4, dropout_p=0.2):
        super().__init__()
        self.query = torch.nn.Linear(128, num_heads * attention_dim)
        self.key = torch.nn.Linear(128, num_heads * attention_dim)
        self.value = torch.nn.Linear(128, num_heads * attention_dim)

    def forward(self, q, k, v, mask=None):
        num_heads = self.query.out_features
        attention_dim = self.query.in_features // self.num_heads
        scale_factor = 1 / math.sqrt(attention_dim)
        q = self.query(q)
        q = q.reshape(size=(-1, batch_size * num_heads, attention_dim))
        k = self.key(k)
        k = k.reshape(size=(-1, batch_size * num_heads, attention_dim))
        v = self.value(v)
        v = v.reshape(size=(-1, batch_size * num_heads, attention_dim))
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


attention_dim = 1

func = Model(attention_dim).to('cpu')


batch_size = 32
length = 12
q = torch.randn(length, batch_size, 128)

batch_size = 32
num = 30
k = torch.randn(num, batch_size, 128)

batch_size = 32
num = 30
v = torch.randn(num, batch_size, 128)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'num_heads'

jit:
'Model' object has no attribute 'num_heads'
'''