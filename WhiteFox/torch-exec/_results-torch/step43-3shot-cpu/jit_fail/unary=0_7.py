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
        self.conv = torch.nn.Conv2d(16, 64, 1, stride=8, padding=0)

    def forward(self, x9):
        v1 = self.conv(x9)
        v1 = torch.permute(v1, (0, 1, 3, 2))
        v1 = torch.contiguous(v1)
        v1 = torch.reshape(v1, (1, 64, 128, 32))
        v2 = v1 * 0.5
        v3 = v1 * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        return v10



func = Model().to('cpu')


x9 = torch.randn(1, 16, 32, 16)

test_inputs = [x9]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'contiguous'

jit:
AttributeError: module 'torch' has no attribute 'contiguous'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''