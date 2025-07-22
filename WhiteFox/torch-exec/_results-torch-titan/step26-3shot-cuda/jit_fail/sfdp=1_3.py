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
        self.linear = torch.nn.Linear(256, 256, bias=False)
        self.dropout = torch.nn.Dropout(0.1)
        self.softmax = torch.nn.Softmax(dim=(- 1))

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = torch.matmul(v1, x2.transpose((- 2), (- 1)))
        scale = 5
        v3 = (v2 / scale)
        v4 = self.softmax(v3)
        v5 = self.dropout(v4)
        output = v5.matmul(x2)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 256, 64)



x2 = torch.randn(1, 64, 256)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (256x64 and 256x256)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 256, 64)),), **{}):
a and b must have same reduction dim, but got [256, 64] X [256, 256].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''