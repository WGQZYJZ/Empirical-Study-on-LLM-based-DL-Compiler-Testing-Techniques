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
        self.conv_t = torch.nn.ConvTranspose2d(8, 9, 2, stride=2)

    def forward(self, x1):
        w1 = self.conv_t(x1)
        w2 = torch.abs(w1)
        w3 = w1.flatten()
        w4 = (torch.sigmoid(w3) - 0.75) * 3
        return w2 + w4.reshape(8, 9, 2, 2)



func = Model().to('cpu')


x1 = torch.randn(8, 8, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[8, 9, 2, 2]' is invalid for input of size 1152

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(36*s0*s2*s3,)), 8, 9, 2, 2), **{}):
shape '[8, 9, 2, 2]' is invalid for input of size 36*s0*s2*s3

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''