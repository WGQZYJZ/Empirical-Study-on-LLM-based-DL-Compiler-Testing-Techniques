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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 10, 1)
        self.linear = torch.nn.Linear(940, 84, bias=True)
        self.tanh = torch.nn.Tanh()

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1.view((- 1), 940)
        z1 = self.linear(v2)
        z2 = torch.tanh(z1)
        return z2




func = ModelTanh().to('cuda')



x1 = torch.randn(255, 3, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 940]' is invalid for input of size 167116800

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(255, 10, 256, 256)), -1, 940), **{}):
shape '[-1, 940]' is invalid for input of size 167116800

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''