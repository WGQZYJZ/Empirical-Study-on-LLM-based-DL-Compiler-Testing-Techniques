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
        self.fc1 = torch.nn.Sequential(torch.nn.Linear(3, 32), torch.nn.ReLU(inplace=True))
        self.fc2 = torch.nn.Sequential(torch.nn.Linear(8, 32), torch.nn.ReLU(inplace=True))

    def forward(self, x1, x2):
        y = torch.cat((x1, x2), dim=1)
        y0 = self.fc1(y)
        y0 = (y + y0)
        y1 = self.fc2(y0)
        y1 = (y0 + y1)
        return y1



func = Model().to('cuda')



x1 = torch.randn(1, 3)



x2 = torch.randn(1, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x11 and 3x32)

jit:
Failed running call_module L__self___fc1_0(*(FakeTensor(..., device='cuda:0', size=(1, 11)),), **{}):
a and b must have same reduction dim, but got [1, 11] X [3, 32].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''