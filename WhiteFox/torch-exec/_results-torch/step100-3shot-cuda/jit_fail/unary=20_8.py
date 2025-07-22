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
        self.conv_t = torch.nn.functional.conv_transpose2d

    def forward(self, x1):
        v1 = self.conv_t(x1, weight=torch.tensor([[[[-0.7576]], [[-0.8314]], [[-0.7894]]], [[[-0.3408]], [[-0.6156]], [[-0.3063]]], [[[1.2174]], [[1.1322]], [[1.2979]]]]), bias=None, stride=(1, 94), padding=(53, 52), dilation=(1, 93))
        v2 = torch.sigmoid(v1)
        return v2



func = Model().to('cuda')


x1 = torch.randn(79, 1, 18, 57)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 3, 1, 1], expected input[79, 1, 18, 57] to have 3 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7baf3f996ec0>(*(FakeTensor(..., device='cuda:0', size=(s0, 1, s1, s2)),), **{'weight': FakeTensor(..., size=(3, 3, 1, 1)), 'bias': None, 'stride': (1, 94), 'padding': (53, 52), 'dilation': (1, 93)}):
Given transposed=1, weight of size [3, 3, 1, 1], expected input[s0, 1, s1, s2] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''