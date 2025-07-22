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
        self.conv_t = torch.nn.ConvTranspose2d(480, 7, 2, stride=2)

    def forward(self, x1):
        x2 = self.conv_t(x1)
        x3 = torch.sigmoid(x2)
        x4 = x2 * 0.5
        x5 = torch.where(x3, x2, x4)
        return x5 + torch.nn.functional.adaptive_avg_pool2d(x5, (1, 1))



func = Model().to('cpu')


x1 = torch.randn(16, 480, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
where expected condition to be a boolean tensor, but got a tensor with dtype Float

jit:
Failed running call_function <built-in method where of type object at 0x744d76d96ec0>(*(FakeTensor(..., size=(s0, 7, 2*s1, 2*s2)), FakeTensor(..., size=(s0, 7, 2*s1, 2*s2)), FakeTensor(..., size=(s0, 7, 2*s1, 2*s2))), **{}):
expected predicate to be bool, got torch.float32

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''