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
        self.conv_t1 = torch.nn.ConvTranspose2d(1, 5, 2, stride=2)
        self.conv_t2 = torch.nn.ConvTranspose2d(5, 19, 3, stride=2, padding=1, output_padding=1)
        self.conv_t3 = torch.nn.ConvTranspose2d(19, 480, 3, stride=2, padding=1, output_padding=1)

    def forward(self, x0):
        t1 = self.conv_t1(x0)
        t1 = t1 > 0
        t1 = t1 * 0.5
        t1 = torch.where(t1, t1, -t1)
        t2 = self.conv_t2(t1)
        t2 = t2 > 0
        t2 = t2 * 0.5
        t2 = torch.where(t2, t2, -t2)
        t3 = self.conv_t3(t2)
        t3 = t3 > 0
        t3 = t3 * 0.5
        t3 = torch.where(t3, t3, -t3)
        return t3



func = Model().to('cpu')


x0 = torch.randn(8, 1, 14, 16)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
where expected condition to be a boolean tensor, but got a tensor with dtype Float

jit:
Failed running call_function <built-in method where of type object at 0x7558b8396ec0>(*(FakeTensor(..., size=(8, 5, 28, 32)), FakeTensor(..., size=(8, 5, 28, 32)), FakeTensor(..., size=(8, 5, 28, 32))), **{}):
expected predicate to be bool, got torch.float32

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''