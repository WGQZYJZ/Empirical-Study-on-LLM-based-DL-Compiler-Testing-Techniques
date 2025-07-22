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
        self.conv1 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)

    def forward(self, x1):
        v0 = torch.nn.functional.interpolate(x1, None, 0.25, 'bilinear', True)
        v1 = self.conv1(v0)
        v2 = torch.nn.functional.interpolate(v1, None, 0.25, 'bilinear', True)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 257, 257)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
OverflowError: cannot convert float infinity to integer


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''