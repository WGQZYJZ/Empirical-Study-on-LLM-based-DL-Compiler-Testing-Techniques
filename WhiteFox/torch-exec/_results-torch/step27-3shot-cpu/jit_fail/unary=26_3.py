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
        self.conv_t = torch.nn.ConvTranspose2d(4, 5, 2, stride=2)

    def forward(self, x):
        y1 = self.conv_t(x.reshape(1, 4, 8, 8))
        y2 = y1 > 0
        y3 = y1 * 0.02
        y4 = torch.where(y2, y1, y3)
        return y4.detach()



func = Model().to('cpu')


x = torch.randn(22, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[1, 4, 8, 8]' is invalid for input of size 88

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(22, 4)), 1, 4, 8, 8), **{}):
shape '[1, 4, 8, 8]' is invalid for input of size 88

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''