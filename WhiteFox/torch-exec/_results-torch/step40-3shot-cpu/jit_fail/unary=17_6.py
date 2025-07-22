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
        self.conv_1 = torch.nn.ConvTranspose2d(3, 64, kernel_size=2)
        self.conv_2 = torch.nn.ConvTranspose2d(64, 128, kernel_size=2, stride=2)

    def forward(self, x1):
        v1 = self.conv_1(x1)
        v2 = F.relu(v1)
        v2 = v2.max_pool2d(3, stride=3)
        v3 = self.conv_2(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute 'max_pool2d'

jit:
Failed running call_method max_pool2d(*(FakeTensor(..., size=(1, 64, 65, 65)), 3), **{'stride': 3}):
'FakeTensor' object has no attribute 'max_pool2d'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''