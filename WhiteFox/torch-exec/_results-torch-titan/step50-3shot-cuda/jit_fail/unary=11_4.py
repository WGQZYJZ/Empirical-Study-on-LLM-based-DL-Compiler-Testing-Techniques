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
        self.conv_transpose = torch.nn.ConvTranspose2d(32, 16, 3, stride=2, padding=(1, 0), dilation=(2, 1))
        self.conv_transpose.weight = torch.nn.Parameter(torch.tensor([[(- 0.6177), 0.5829, (- 0.964)]], dtype=torch.float32))
        self.conv_transpose.bias = torch.nn.Parameter(torch.tensor([[(- 1.6924)]], dtype=torch.float32))

    def forward(self, x1):

        def helper(x):
            v1 = self.conv_transpose(x)
            v2 = torch.clamp_min((v1 + 1), (- 3))
            return (torch.clamp_max(v2, 2) / 11)
        v3 = torch.sigmoid(helper(torch.tanh(x1)))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 32, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
weight should have at least three dimensions

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 32, 64, 64)),), **{}):
expected stride to be a single integer value or a list of 0 values to match the convolution dimensions, but got stride=[2, 2]

from user code:
   File "<string>", line 29, in forward
  File "<string>", line 26, in helper


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''