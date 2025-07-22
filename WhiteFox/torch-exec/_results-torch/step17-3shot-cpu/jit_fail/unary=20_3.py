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
        self.conv_t = torch.nn.ConvTranspose2d(96, 14, kernel_size=(3, 3))

    def forward(self, x):
        v1 = self.conv_t(x)
        v2 = torch.sigmoid(v1)
        v3 = v2.view([1, 14, 44, 44])
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 96, 44, 44)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 14, 44, 44]' is invalid for input of size 29624

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 14, 46, 46)), [1, 14, 44, 44]), **{}):
shape '[1, 14, 44, 44]' is invalid for input of size 29624

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''