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
        self.conv = torch.nn.ConvTranspose2d(5, 1, kernel_size=2, stride=2, padding=0, output_padding=0, groups=1, dilation=1, bias=True)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - None
        return v2



func = Model().to('cpu')


x = torch.randn(1, 5, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for -: 'Tensor' and 'NoneType'

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(1, 1, 128, 128)), None), **{}):
unsupported operand type(s) for -: 'FakeTensor' and 'NoneType'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''