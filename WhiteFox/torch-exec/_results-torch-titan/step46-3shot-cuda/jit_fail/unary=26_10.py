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
        self.conv_t = torch.nn.ConvTranspose2d(1, 3, 1, stride=2, padding=21, bias=True)

    def forward(self, x5):
        z1 = self.conv_t(x5)
        z2 = (z1 > 0)
        z3 = (z1 * (- 0.752))
        z4 = torch.where(z2, z1, z3)
        return torch.nn.functional.interpolate(z4, scale_factor=[1.0, 1.0])




func = Model().to('cuda')



x5 = torch.randn(3, 1, 7, 31)


test_inputs = [x5]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -29: [3, 3, -29, 19]

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(3, 1, 7, 31)),), **{}):
Trying to create tensor with negative dimension -29: [3, 3, -29, 19]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''