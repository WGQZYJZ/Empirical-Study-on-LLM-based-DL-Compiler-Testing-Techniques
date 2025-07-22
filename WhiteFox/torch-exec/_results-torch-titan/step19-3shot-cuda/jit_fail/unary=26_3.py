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
        self.conv_t = torch.nn.ConvTranspose3d(480, 480, 2, stride=2)
        self.linear = torch.nn.Linear((480 * 480), 7)

    def forward(self, x1):
        x2 = self.conv_t(x1)
        x3 = x2.view(16, (480 * 480))
        x4 = self.linear(x3)
        return x4




func = Model().to('cuda')



x1 = torch.randn(16, 480, 10, 10, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[16, 230400]' is invalid for input of size 61440000

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(16, 480, 20, 20, 20)), 16, 230400), **{}):
shape '[16, 230400]' is invalid for input of size 61440000

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''