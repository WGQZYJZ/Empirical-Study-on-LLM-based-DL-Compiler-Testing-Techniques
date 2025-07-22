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
        self.linear1 = torch.nn.Linear(256, 128, bias=False)
        self.dropout = torch.nn.Dropout(0.1)
        self.linear2 = torch.nn.Linear(128, 256, bias=False)

    def forward(self, x1, x2):
        y1 = self.linear1(x1)
        y2 = self.linear2(x2)
        z1 = torch.matmul(y1, y2.transpose((- 2), (- 1)))
        z2 = self.dropout(z1)
        z3 = torch.matmul(z2, y1)
        return (z1, z3)



func = Model().to('cuda')



x1 = torch.randn(1, 256, 10)



x2 = torch.randn(1, 10, 256)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (256x10 and 256x128)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 256, 10)),), **{}):
a and b must have same reduction dim, but got [256, 10] X [256, 128].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''