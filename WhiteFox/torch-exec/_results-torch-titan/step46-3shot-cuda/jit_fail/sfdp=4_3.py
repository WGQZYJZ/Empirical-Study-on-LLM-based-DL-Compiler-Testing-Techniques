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



class Module1(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = (x + x)
        x = (x + x)
        return x




class Module0(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(4, 4, 1)
        self.conv2 = Module1()

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        return x




class model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(18, 36)
        self.linear2 = torch.nn.Linear(36, 72)

    def forward(self, x):
        x = self.linear1(x)
        x = self.linear2(x)
        return x




func = model().to('cuda')



x = torch.randn(1, 4, 12, 12)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (48x12 and 18x36)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 4, 12, 12)),), **{}):
a and b must have same reduction dim, but got [48, 12] X [18, 36].

from user code:
   File "<string>", line 51, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''