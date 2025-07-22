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
        torch.manual_seed(3)
        self.conv1 = torch.nn.Conv1d(1, 1, 3, stride=2)
        torch.manual_seed(3)
        self.conv2 = torch.nn.Conv1d(1, 1, 3, stride=2)
        self.bn = torch.nn.BatchNorm1d(1)
        self.relu = torch.nn.ReLU()
        self.mp = torch.nn.MaxPool1d(2)

    def forward(self, input):
        c = self.conv1(input)
        a = self.bn(c)
        d = self.relu(c)
        e = self.conv2(d)
        b = self.mp(e)
        return b



func = Model().to('cpu')


input = torch.randn(1, 1, 7)

test_inputs = [input]

# JIT_FAIL
'''
direct:
max_pool1d() Invalid computed output size: 0

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x7d0deed62d30>(*(FakeTensor(..., size=(1, 1, 1)), 2, 2, 0, 1), **{'ceil_mode': False, 'return_indices': False}):
max_pool1d() Invalid computed output size: 0

from user code:
   File "<string>", line 30, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 134, in forward
    return F.max_pool1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''