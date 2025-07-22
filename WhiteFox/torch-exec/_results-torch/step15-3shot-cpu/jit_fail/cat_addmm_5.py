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

class Model1(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = torch.abs(x)
        x = torch.nn.functional.interpolate(x, mode=nn.Upsample.NEAREST)
        return x



func = Model1().to('cpu')


x = torch.randn(1, 1, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
type object 'Upsample' has no attribute 'NEAREST'

jit:
Failed running call_function <function interpolate at 0x76c84041a0d0>(*(FakeTensor(..., size=(1, 1, 2, 2)),), **{'mode': None}):
either size or scale_factor should be defined

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''