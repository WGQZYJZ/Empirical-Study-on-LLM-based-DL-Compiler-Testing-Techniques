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
        self.fc1 = torch.nn.Linear(10, 24)
        self.fc2 = torch.nn.Linear(24, 8)

    def forward(self, x1, x2):
        v1 = self.fc1(x1)
        v2 = self.fc2(v1)
        v3 = torch.matmul(x2, v2.transpose(1, 0))
        v4 = v3.softmax(dim=(- 1))
        v5 = v4.dropout(p=0)
        return v5.matmul(v1)



func = Model().to('cuda')



x1 = torch.randn(10, 10, 1)



x2 = torch.randn(20, 10, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (100x1 and 10x24)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(10, 10, 1)),), **{}):
a and b must have same reduction dim, but got [100, 1] X [10, 24].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''