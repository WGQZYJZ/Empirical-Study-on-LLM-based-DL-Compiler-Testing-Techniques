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

    def __init__(self, hidden):
        super().__init__()
        self.query = torch.nn.Linear(hidden, hidden, bias=False)
        self.key = torch.nn.Linear(hidden, hidden, bias=False)
        self.value = torch.nn.Linear(hidden, hidden, bias=False)

    def forward(self, x1, x2):
        v1 = self.query(x1)
        v2 = self.key(x2)
        qk = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        qk = qk.div(math.sqrt(hidden))
        qk.masked_fill_(x3, float('-inf'))
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn = (self.value(x2) @ attn_weight.transpose((- 2), (- 1)))
        return attn



hidden = 1

func = Model(hidden).to('cuda')



x1 = torch.randn(2, 64, 128)



x2 = torch.randn(2, 4, 128)



x3 = torch.randint(0, 2, (2, 64, 4))


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''