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
        self.conv = torch.nn.Conv2d(3, 32, 1, stride=1, padding=1)

    def forward(self, x1, bias1=None, other=None):
        v1 = self.conv(x1)
        if ((bias1 is None) and (other is not None)):
            other = torch.randn(v1.shape)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 3, 512, 75)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for +: 'Tensor' and 'NoneType'

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(3, 32, 514, 77)), None), **{}):
unsupported operand type(s) for +: 'FakeTensor' and 'NoneType'

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''