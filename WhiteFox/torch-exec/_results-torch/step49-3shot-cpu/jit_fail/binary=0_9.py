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
        self.layer_one = torch.nn.Conv2d(16, 15, 1, stride=1, padding=2)

    def forward(self, x, other_conv=None, other_dense=None, x1=None):
        if other_conv == None:
            other_conv = torch.randn(1, 10, 16, 16)
        if x1 == None:
            x1 = torch.randn(1, 1, 256, 256)
        v1 = self.layer_one(x)
        var2 = v1 + other_conv
        if other_dense == None:
            other_dense = torch.randn(1, 10)
        var3 = var2 + other_dense
        return var3



func = Model().to('cpu')


x = torch.randn(1, 16, 256, 256)

x1 = torch.randn(1, 1, 256, 256)

test_inputs = [x, x1]

# JIT_FAIL
'''
direct:
The size of tensor a (260) must match the size of tensor b (256) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 15, 260, 260)), FakeTensor(..., size=(1, 1, 256, 256))), **{}):
Attempting to broadcast a dimension of length 256 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 256, 256]); but expected shape should be broadcastable to [1, 15, 260, 260]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''