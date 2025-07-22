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

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 4, bias=False)

    def forward(self, x1, x2):
        qk = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1))
        qk = qk + self.mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ x1
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 4, 2)

x2 = torch.randn(1, 2, 4)

x3 = torch.randn(1, 1, 1, 4)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''