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

    def forward(self, input, other=None):
        t1 = torch.nn.functional.max_pool2d(input, kernel_size=(3, 3), stride=1, padding=(2, 2), ceil_mode=False, return_indices=False, dilation=1)
        if other == None:
            other = []
        t2 = t1 + other
        return t2



func = Model().to('cpu')


input = torch.randn(2, 3, 64, 64)

test_inputs = [input]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x7698daba1ee0>(*(FakeTensor(..., size=(2, 3, 64, 64)),), **{'kernel_size': (3, 3), 'stride': 1, 'padding': (2, 2), 'ceil_mode': False, 'return_indices': False, 'dilation': 1}):
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''