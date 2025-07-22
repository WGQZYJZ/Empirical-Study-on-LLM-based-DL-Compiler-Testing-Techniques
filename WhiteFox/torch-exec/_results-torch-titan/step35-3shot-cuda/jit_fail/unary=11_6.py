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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, 5, dilation=2, bias=False)
        self.dense = torch.nn.Linear(264, 128)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 + 3)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = (v4 / 6)
        v6 = v5.flatten(start_dim=1, end_dim=(- 1))
        v7 = self.dense(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x4800 and 264x128)

jit:
Failed running call_module L__self___dense(*(FakeTensor(..., device='cuda:0', size=(1, 4800)),), **{}):
a and b must have same reduction dim, but got [1, 4800] X [264, 128].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''