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
        self.conv = torch.nn.Conv2d(9, 9, 3, stride=1, padding=1)
        negative_slope = 1.0

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 > 0)
        v3 = (v1 * negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 9, 43, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'negative_slope' is not defined

jit:
name 'negative_slope' is not defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''