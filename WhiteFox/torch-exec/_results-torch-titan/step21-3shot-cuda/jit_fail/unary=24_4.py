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
        self.conv = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x, negative_slope):
        v1 = self.conv(x)
        v2 = (v1 > 0)
        v3 = (v1 * negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 8, 64, 64)

x = 1

test_inputs = [x1, x]

# JIT_FAIL
'''
direct:
name 'v5' is not defined

jit:
name 'v5' is not defined

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''