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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 32, kernel_size=5, stride=1)
        self.linear = torch.nn.Linear(in_features=16, out_features=16)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v1 = v1.flatten()
        v1 = self.linear(v1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x41472 and 16x16)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(41472,)),), **{}):
a and b must have same reduction dim, but got [1, 41472] X [16, 16].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''