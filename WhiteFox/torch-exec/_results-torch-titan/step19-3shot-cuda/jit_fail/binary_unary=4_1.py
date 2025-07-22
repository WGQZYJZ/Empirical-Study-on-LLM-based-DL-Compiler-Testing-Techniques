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
        self.linear = torch.nn.Linear(4, 3, bias=False)

    def forward(self, x1, other=None):
        if (other is None):
            other = torch.randn(3, 4)
        elif (other.dim() != 2):
            raise ValueError(f'The shape of "other" is expected to be [3, 4], but got {list(other.shape)}')
        v1 = self.linear(x1)
        v2 = (v1 + other)
        v3 = F.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(2, 4, 288, 352)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2304x352 and 4x3)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(2, 4, 288, 352)),), **{}):
a and b must have same reduction dim, but got [2304, 352] X [4, 3].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''