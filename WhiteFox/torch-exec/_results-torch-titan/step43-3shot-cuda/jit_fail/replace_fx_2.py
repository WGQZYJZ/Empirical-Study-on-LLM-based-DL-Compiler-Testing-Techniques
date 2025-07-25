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
        self.conv1 = torch.nn.Conv2d(1, 1, 3)
        self.dense1 = torch.nn.Linear(20, 20)
        self.dense2 = torch.nn.Linear(20, 20)
        self.relu1 = torch.nn.ReLU()
        self.relu2 = torch.nn.ReLU()

    def forward(self, x1):
        x2 = self.conv1(x1)
        x3 = self.relu1(x2)
        x4 = F.max_pool2d(x3, 2, 2)
        x5 = torch.flatten(x4, 1)
        x6 = self.dense1(x5)
        x7 = self.relu2(x6)
        x8 = self.dense2(x5)
        x9 = self.relu2(x8)
        x10 = torch.rand_like(x8)
        return x7




func = Model().to('cuda')



x1 = torch.randn(1, 1, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size: (1x1x1). Calculated output size: (1x0x0). Output size is too small

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x78046a5daca0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 1)), 2, 2), **{}):
Given input size: (1x1x1). Calculated output size: (1x0x0). Output size is too small

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''