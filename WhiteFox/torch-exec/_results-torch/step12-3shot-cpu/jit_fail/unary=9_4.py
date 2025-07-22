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

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.add(v1, 3)
        v3 = torch.clamp(v2)
        v4 = torch.clamp_max(v3, 6)
        v5 = torch.div(v4, 6)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
torch.clamp: At least one of 'min' or 'max' must not be None

jit:
Failed running call_function <built-in method clamp of type object at 0x7f386b796ec0>(*(FakeTensor(..., size=(1, 8, 66, 66)),), **{}):
clamp called but both min and max are none!

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''