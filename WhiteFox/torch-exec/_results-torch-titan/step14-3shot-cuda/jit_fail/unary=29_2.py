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

    def __init__(self, min_value=3, max_value=2.3):
        super().__init__()
        self.max_pool = torch.nn.MaxPool2d(2, 1)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 2, stride=2)
        self.conv_transpose.weight.data = torch.Tensor([[[[1, 1, 0], [1, 1, 1], [0, 1, 1]]]])
        self.conv_transpose.bias.data = torch.Tensor([(- 4), (- 3), (- 2), (- 1), 0, 1, 2, 3])
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.max_pool(x1)
        v2 = self.conv_transpose(v1)
        v3 = torch.clamp_min(v2, self.min_value)
        v4 = torch.clamp_max(v3, self.max_value)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size: (3x1x1). Calculated output size: (3x0x0). Output size is too small

jit:
Failed running call_module L__self___max_pool(*(FakeTensor(..., device='cuda:0', size=(1, 3, 1, 1)),), **{}):
Given input size: (3x1x1). Calculated output size: (3x0x0). Output size is too small

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''