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

    def forward(self, x1, x2, x3):
        x1 = torch.mm(x2, x3)
        x2 = torch.add(x1, x2)
        x3 = torch.cat([x2], 0)
        return (x3, x1)


func = Model().to('cpu')


x1 = torch.randn(1, 10)

x2 = torch.randn(10, 7)

x3 = torch.randn(7, 10)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (7) at non-singleton dimension 1

jit:
Failed running call_function <built-in method add of type object at 0x71ddb4396ec0>(*(FakeTensor(..., size=(10, 10)), FakeTensor(..., size=(10, 7))), **{}):
Attempting to broadcast a dimension of length 7 at -1! Mismatching argument at index 1 had torch.Size([10, 7]); but expected shape should be broadcastable to [10, 10]

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''