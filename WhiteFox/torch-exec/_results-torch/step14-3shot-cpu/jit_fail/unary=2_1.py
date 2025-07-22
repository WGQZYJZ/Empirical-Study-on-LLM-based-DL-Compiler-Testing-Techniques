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
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 1, kernel_size=4, stride=4, padding=0)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        x2 = v1.reshape(1)
        return x2



func = Model().to('cpu')


x1 = torch.randn(16, 16, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1]' is invalid for input of size 4096

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(s0, 1, 4*s2, 4*s3)), 1), **{}):
shape '[1]' is invalid for input of size 16*s0*s2*s3

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''