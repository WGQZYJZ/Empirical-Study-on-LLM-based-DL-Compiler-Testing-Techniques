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

class MyModel(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, inp):
        return torch.transpose(x1, 0, 1) + inp



func = MyModel().to('cpu')


x1 = torch.randn(3, 5)

x2 = torch.randn(1, 5)

inp = torch.randn(7, 8)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(5, 3)), FakeTensor(..., size=(7, 8))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([7, 8]); but expected shape should be broadcastable to [5, 3]

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''