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
        self.conv = torch.nn.Conv2d(3, 32, kernel_size=(3, 5), stride=(4, 4), padding=0, dilation=(0, 0))

    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other == None:
            other = torch.randn(1, v1.shape[1], v1.shape[2] + 1, v1.shape[3] + 1)
        v2 = v1 + other
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
dilation should be greater than zero, but got [0, 0]

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 32, (((s1 - 1)//4)) + 1, (((s2 - 1)//4)) + 1)), FakeTensor(..., size=(1, 32, (((s1 - 1)//4)) + 2, (((s2 - 1)//4)) + 2))), **{}):
The size of tensor a ((((s2 - 1)//4)) + 1) must match the size of tensor b ((((s2 - 1)//4)) + 2) at non-singleton dimension 3)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''