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
        self.linear = torch.nn.Linear(32, 64, bias=True)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 * torchvision.ops.misc.clamp_by_value((v1 + 3), 0.0, 6.0))
        v3 = (v2 / 6)
        return v3



func = Model().to('cuda')



x1 = torch.randn(2, 32, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (192x3 and 32x64)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(2, 32, 3, 3)),), **{}):
a and b must have same reduction dim, but got [192, 3] X [32, 64].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''