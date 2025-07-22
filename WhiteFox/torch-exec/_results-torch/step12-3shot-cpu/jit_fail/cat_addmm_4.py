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

    def forward(self, x1):
        v1 = torch.addmm(x1, torch.rand(64, 64), torch.rand(64, 64))
        return [v1]


func = Model().to('cpu')


x1 = torch.randn(64, 50, 20)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expand(torch.FloatTensor{[64, 50, 20]}, size=[64, 64]): the number of sizes provided (2) must be greater or equal to the number of dimensions in the tensor (3)

jit:
Failed running call_function <built-in method addmm of type object at 0x719f52f96ec0>(*(FakeTensor(..., size=(64, 50, 20)), FakeTensor(..., size=(64, 64)), FakeTensor(..., size=(64, 64))), **{}):
Attempting to broadcast a dimension of length 20 at -1! Mismatching argument at index 1 had torch.Size([64, 50, 20]); but expected shape should be broadcastable to [1, 64, 64]

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''