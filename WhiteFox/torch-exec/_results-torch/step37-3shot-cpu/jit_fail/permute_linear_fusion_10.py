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
        self.conv = torch.nn.ConvTranspose2d(2, 2, 2, groups=2)

    def forward(self, x):
        x = x.view(x.shape[0] * 2, 1, x.shape[2], x.shape[3])
        x = self.conv(x)
        return x.view(x.shape[0] // 2, x.shape[1] * x.shape[2] * x.shape[3])



func = Model().to('cpu')


x = torch.randn(1, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
tuple index out of range

jit:
IndexError: list index out of range

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''