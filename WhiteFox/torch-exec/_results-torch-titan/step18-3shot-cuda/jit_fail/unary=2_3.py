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
        self.t1 = torch.nn.ConvTranspose2d(3, 5, kernel_size=(1, 1), stride=(1, 2), padding=(0, 1))
        self.t2 = torch.nn.ConvTranspose2d(1, 8, 1, stride=1, padding=1, dilation=(2, 4))

    def forward(self, x1):
        v1 = self.t1(x1)
        v2 = (v1 * 0.5)
        v3 = ((v1 * v1) * v1)
        v4 = (v3 * 0.044715)
        v5 = (v1 + v4)
        v6 = (v5 * 0.7978845608028654)
        v7 = torch.tanh(v6)
        v8 = (v7 + 1)
        v9 = (v2 * v8)
        v10 = self.t2(v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(1, 3, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 8, 1, 1], expected input[1, 5, 5, 7] to have 1 channels, but got 5 channels instead

jit:
Failed running call_module L__self___t2(*(FakeTensor(..., device='cuda:0', size=(1, 5, 5, 7)),), **{}):
Given transposed=1, weight of size [1, 8, 1, 1], expected input[1, 5, 5, 7] to have 1 channels, but got 5 channels instead

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''