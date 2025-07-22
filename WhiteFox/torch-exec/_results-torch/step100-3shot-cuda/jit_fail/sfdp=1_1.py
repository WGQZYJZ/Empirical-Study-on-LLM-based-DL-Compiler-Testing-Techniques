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

    def __init__(self, dim_size, num_heads):
        super().__init__()
        self.key = torch.nn.Linear(dim_size, dim_size)
        self.query = torch.nn.Linear(dim_size, dim_size)
        self.value = torch.nn.Linear(dim_size, dim_size)

    def forward(self, x1):
        k = self.key(x1)
        q = self.query(x1)
        v = self.value(x1)
        qk = torch.matmul(k, q.transpose(-2, -1))
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(v)
        return (output, mask)


dim_size = 1
num_heads = 1
func = Model(128, 4).to('cuda')


x1 = torch.randn(4, 128)

mask = torch.zeros(4, 4)

test_inputs = [x1, mask]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''