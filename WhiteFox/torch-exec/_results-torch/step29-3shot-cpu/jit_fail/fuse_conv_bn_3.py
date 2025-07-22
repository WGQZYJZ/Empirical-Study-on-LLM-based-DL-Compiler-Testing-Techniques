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
        self.layer = torch.nn.Sequential(torch.nn.Conv2d(5, 5, 2), torch.nn.BatchNorm2d(5))

    def forward(self, x4, x5):
        out1 = [self.layer(x4), self.layer(x5)]
        out2 = [self.layer(x4), self.layer(x5)]
        return (out1[0], out1[1], out2[0] + out2[1])



func = Model().to('cpu')


x4 = torch.randn(4, 5, 4, 4)

x5 = torch.randn(2, 5, 4, 4)

test_inputs = [x4, x5]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, 5, 3, 3)), FakeTensor(..., size=(2, 5, 3, 3))), **{}):
The size of tensor a (s0) must match the size of tensor b (2) at non-singleton dimension 0)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''