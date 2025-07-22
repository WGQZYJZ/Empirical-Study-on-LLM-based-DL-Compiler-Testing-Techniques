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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, other=1, bias=None):
        t1 = self.conv(x1)
        b1 = torch.add(t1, bias)
        v2 = (b1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)



bias = torch.randn(1, 8, 32, 32)


test_inputs = [x1, bias]

# JIT_FAIL
'''
direct:
add(): argument 'other' (position 2) must be Tensor, not NoneType

jit:
Failed running call_function <built-in method add of type object at 0x73d749a699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 34, 34)), None), **{}):
add(): argument 'other' (position 2) must be Tensor, not NoneType

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''