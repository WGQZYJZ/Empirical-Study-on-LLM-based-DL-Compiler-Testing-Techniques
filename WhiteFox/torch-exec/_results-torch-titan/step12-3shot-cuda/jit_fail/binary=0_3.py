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
        self.pool = torch.nn.AvgPool2d((66, 56))

    def forward(self, x1, other=True):
        v1 = self.pool(x1)
        if (other == True):
            other = torch.randn(v1.shape)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 4, 48, 48)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size: (4x48x48). Calculated output size: (4x0x0). Output size is too small

jit:
Failed running call_module L__self___pool(*(FakeTensor(..., device='cuda:0', size=(1, 4, 48, 48)),), **{}):
Given input size: (4x48x48). Calculated output size: (4x0x0). Output size is too small

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''