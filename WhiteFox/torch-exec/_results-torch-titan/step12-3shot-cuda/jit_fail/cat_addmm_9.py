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
        self.fc = torch.nn.Linear(96, 72)
        self.fc1 = torch.nn.Linear(72, 12)
        self.fc2 = torch.nn.Linear(12, 3)

    def forward(self, x1):
        v1 = torch.cat([self.fc(x1), self.fc1(x1), self.fc2(x1)], dim=0)
        return v1



func = Model().to('cuda')



x1 = torch.randn(1, 96)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x96 and 72x12)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(1, 96)),), **{}):
a and b must have same reduction dim, but got [1, 96] X [72, 12].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''