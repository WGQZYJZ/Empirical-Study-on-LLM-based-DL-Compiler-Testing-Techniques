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
        super(Model, self).__init__()
        self.conv_t1 = torch.nn.ConvTranspose2d(64, 64, 3, stride=1, padding=1, output_padding=1, groups=2)
        self.conv_t2 = torch.nn.ConvTranspose2d(64, 32, 3, stride=2, padding=1, output_padding=1)

    def forward(self, x0):
        identity = x0
        x3 = self.conv_t1(x0)
        x4 = self.conv_t2(x3)
        out = (x4 - identity)
        return out




func = Model().to('cuda')

x0 = 1

test_inputs = [x0]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___conv_t1(*(1,), **{}):
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''