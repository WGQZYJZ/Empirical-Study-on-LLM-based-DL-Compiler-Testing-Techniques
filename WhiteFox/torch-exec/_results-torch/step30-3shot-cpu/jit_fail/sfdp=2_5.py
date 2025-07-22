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

    def __init__(self, dropout_p, dim, num_heads):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.q_weight = torch.nn.Parameter(torch.randn(num_heads, dim, dim))
        self.k_weight = torch.nn.Parameter(torch.randn(num_heads, dim, dim))
        self.v_weight = torch.nn.Parameter(torch.randn(num_heads, dim, dim))
        self.out_weight = torch.nn.Parameter(torch.randn(num_heads, dim, dim))
        self.bias = torch.nn.Parameter(torch.randn(num_heads, dim))
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x1):
        (q, k, v) = torch.chunk(x1, self.num_heads, dim=1)
        q = torch.matmul(q, self.q_weight.transpose(-2, -1))
        k = torch.matmul(k, self.k_weight.transpose(-2, -1))
        v = torch.matmul(v, self.v_weight.transpose(-2, -1))
        scaled_qk = q.softmax(dim=2) * k.softmax(dim=2)
        scaled_qk = scaled_qk.softmax(dim=2) * k.softmax(dim=2)
        scaled_qk = scaled_qk.softmax(dim=2)
        out = self.dropout(scaled_qk).matmul(self.value)
        out = out.transpose(1, 2)
        out = out.reshape(-1, self.dim * self.num_heads)
        out = torch.matmul(out, self.out_weight.transpose(0, 1)) + self.bias
        return out


dropout_p = 1
dim = 1
num_heads = 1

func = Model(dropout_p, dim, num_heads).to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
chunk(): argument 'input' (position 1) must be Tensor, not int

jit:
chunk(): argument 'input' (position 1) must be Tensor, not int
'''