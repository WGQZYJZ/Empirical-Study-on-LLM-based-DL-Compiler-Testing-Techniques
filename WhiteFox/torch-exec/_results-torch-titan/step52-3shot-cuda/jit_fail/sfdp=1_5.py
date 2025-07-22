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

    def __init__(self, query, key, value):
        super().__init__()
        w = torch.randn(query.size(0), query.size(1))
        b = torch.randn(query.size(0))
        self.query = query
        self.key = key
        self.value = value
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.weights = torch.nn.Parameter(w)
        self.bias = torch.nn.Parameter(b)

    def forward(self, q1):
        v1 = torch.matmul(q1, self.key.transpose((- 2), (- 1)))
        v2 = v1.div(0.72)
        v3 = self.softmax(v2)
        v4 = nn.functional.dropout(v3, p=0.3)
        o = torch.matmul(v4, self.value)
        o = (o + self.bias)
        o = torch.matmul(o, self.weights)
        return o




query = torch.randn(10, 20, 64)


key = torch.randn(6, 20, 100)


value = torch.randn(6, 20, 100)

func = Model(query, key, value).to('cuda')



query = torch.randn(10, 20, 64)



key = torch.randn(6, 20, 100)



x1 = torch.randn(10, 20, 64)


test_inputs = [query, key, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''