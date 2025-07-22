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
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.linear1 = torch.nn.Linear(1280, 1024)
        self.linear2 = torch.nn.Linear(1024, 256)

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = self.linear1(t1)
        t3 = self.linear2(t2)
        return t3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (198x66 and 1280x1024)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 66, 66)),), **{}):
a and b must have same reduction dim, but got [198, 66] X [1280, 1024].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''