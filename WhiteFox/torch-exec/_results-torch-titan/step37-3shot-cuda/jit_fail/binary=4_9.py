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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1)
        self.layer0 = torch.nn.Linear(8, 8, bias=False)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1.view(v1.shape[0], (- 1))
        v3 = self.layer0(v2)
        return torch.cat((v1, v3), 1)



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x32768 and 8x8)

jit:
Failed running call_module L__self___layer0(*(FakeTensor(..., device='cuda:0', size=(1, 32768)),), **{}):
a and b must have same reduction dim, but got [1, 32768] X [8, 8].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''