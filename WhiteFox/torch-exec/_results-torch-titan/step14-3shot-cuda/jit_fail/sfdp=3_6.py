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

    def __init__(self, query, key, value, dropout_p):
        super().__init__()
        self.query = query
        self.key = key
        self.value = value
        self.dropout_p = dropout_p

    def forward(self, x1):
        v1 = torch.matmul(self.query, self.key.transpose((- 2), (- 1)))
        v2 = (v1 * x1)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=self.dropout_p)
        output = torch.matmul(v4, self.value)
        return v4




query = torch.randn(64, 64, 128)


key = torch.randn(64, 128, 128)


value = torch.randn(64, 128, 128)


dropout_p = 0.5

func = Model(query, key, value, dropout_p).to('cuda')



query = torch.randn(64, 64, 128)



key = torch.randn(64, 128, 128)



x1 = torch.randn(1, 64, 128)


test_inputs = [query, key, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''