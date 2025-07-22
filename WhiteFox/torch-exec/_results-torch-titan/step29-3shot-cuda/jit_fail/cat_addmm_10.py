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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 2)
        self.bias = nn.Parameter(torch.randn(2, 1))

    def forward(self, x):
        x = self.layers(x)
        x = torch.stack([x, (x + self.bias)], dim=1)
        return x




func = Model().to('cuda')



x = torch.randn(1, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
stack expects each tensor to be equal size, but got [1, 2] at entry 0 and [2, 2] at entry 1

jit:
Failed running call_function <built-in method stack of type object at 0x7face4e699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 2)), FakeTensor(..., device='cuda:0', size=(2, 2))],), **{'dim': 1}):
stack expects each tensor to be equal size, but got torch.Size([1, 2]) at entry 0and torch.Size([2, 2]) at entry 1

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''