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

class Attention(nn.Module):

    def __init__(self, d_model, dropout_p, scale):
        super().__init__()
        self.d_model = d_model
        self.dropout = nn.Dropout(p=dropout_p)
        self.q = nn.Linear(d_model, d_model)
        self.k = nn.Linear(d_model, d_model)
        self.v = nn.Linear(d_model, d_model)
        self.scale = torch.sqrt(torch.FloatTensor([scale]))

    def forward(self, q, k, v, mask=None):
        (batch_size, len_q, d_model) = q.shape
        (batch_size, len_k, d_model) = k.shape
        (batch_size, len_v, d_model) = v.shape
        q = self.q(q).view(batch_size, len_q, self.h, self.d_k).permute(0, 2, 1, 3)
        k = self.k(k).view(batch_size, len_k, self.h, self.d_k).permute(0, 2, 3, 1)
        v = self.v(v).view(batch_size, len_v, self.h, self.d_k).permute(0, 2, 1, 3)
        scaled_attention = torch.matmul(q / self.scale, k)
        attention = nn.functional.softmax(scaled_attention, dim=-1)
        if mask is not None:
            attention = attention.masked_fill(mask == 0, -10000.0)
        output = torch.matmul(attention, v).transpose(1, 2).contiguous().view(batch_size, len_q, -1)
        return self.dropout(output)


d_model = 32
dropout_p = 0.6
scale = 1

func = Attention(d_model, dropout_p, scale).to('cpu')


d_model = 32
x1 = torch.randn(1, 10, d_model)

d_model = 32
x2 = torch.randn(1, 20, d_model)

d_model = 32
x3 = torch.randn(1, 20, d_model)

mask = torch.zeros(1, 10, 20)

test_inputs = [x1, x2, x3, mask]

# JIT_FAIL
'''
direct:
'Attention' object has no attribute 'h'

jit:
'Attention' object has no attribute 'h'
'''