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
        self.conv1 = torch.nn.Conv2d(10, 12, 3, 1, 0)
        self.conv_transpose = torch.nn.ConvTranspose2d(12, 18, 2, 1, 4)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv_transpose(v1)
        v3 = (v2 * 0.5)
        v4 = ((v2 * v2) * v2)
        v5 = (v4 * 0.044715)
        v6 = (v2 + v5)
        v7 = (v6 * 0.7978845608028654)
        v8 = torch.tanh(v7)
        v9 = (v8 + 1)
        v10 = (v3 * v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(3, 10, 6, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -3: [3, 18, -3, -4]

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(3, 12, 4, 3)),), **{}):
Trying to create tensor with negative dimension -3: [3, 18, -3, -4]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''