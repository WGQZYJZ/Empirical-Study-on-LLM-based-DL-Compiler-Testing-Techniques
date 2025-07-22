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




func = Model().to('cuda')



input = torch.randn(1, 1, 7)


test_inputs = [input]

# JIT_FAIL
'''
direct:
max_pool1d() Invalid computed output size: 0

jit:
Failed running call_module L__self___mp(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1)),), **{}):
max_pool1d() Invalid computed output size: 0

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''