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
        self.conv = torch.nn.Conv2d(3, 7, 1, stride=1, padding=1)

    def forward(self, x1, other=1, padding1=None):
        v1 = self.conv(x1)
        if (None in (padding1, padding2)):
            v2 = ((v1 * v1) / v1)
            return torch.transpose(v1, 1, 1)
        else:
            v2 = ((v1 - v1) * 1)
            return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'padding2' is not defined

jit:
name 'padding2' is not defined

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''