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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(1, 16, 1, stride=2, padding=1)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(16, 1, 1, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.conv_transpose_2(v1)
        v3 = torch.reshape(v2, (1, 16, 8, 8))
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 1, 8, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 16, 8, 8]' is invalid for input of size 529

jit:
Failed running call_function <built-in method reshape of type object at 0x7f3c59b96ec0>(*(FakeTensor(..., size=(1, 1, 23, 23)), (1, 16, 8, 8)), **{}):
shape '[1, 16, 8, 8]' is invalid for input of size 529

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''