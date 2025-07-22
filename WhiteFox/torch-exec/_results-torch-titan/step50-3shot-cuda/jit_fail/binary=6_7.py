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



class Other_model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(640, 136)

    def forward(self, x1):
        x2 = x1.reshape(1, 1360)
        v1 = self.linear(x2)
        return v1



func = Other_model().to('cuda')



__other__ = torch.randn(1, 3, 64, 64)


test_inputs = [__other__]

# JIT_FAIL
'''
direct:
shape '[1, 1360]' is invalid for input of size 12288

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), 1, 1360), **{}):
shape '[1, 1360]' is invalid for input of size 12288

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''