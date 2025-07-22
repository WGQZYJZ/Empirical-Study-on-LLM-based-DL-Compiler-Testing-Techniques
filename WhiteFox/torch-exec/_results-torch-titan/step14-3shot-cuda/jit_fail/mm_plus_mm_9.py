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
        self.linear1 = nn.Linear(64, 128)
        self.linear2 = nn.Linear(128, 64)

    def forward(self, x):
        x1 = self.linear1(x)
        x2 = self.linear2(x1)
        return (x1 + x2)



func = Model().to('cuda')


inputsize = 128


batchsize = 2



input = torch.randint(high=64, size=(batchsize, inputsize)).float()


test_inputs = [input]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x128 and 64x128)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(2, 128)),), **{}):
a and b must have same reduction dim, but got [2, 128] X [64, 128].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''