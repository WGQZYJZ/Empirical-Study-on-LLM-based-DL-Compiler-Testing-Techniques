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
        self.linear = torch.nn.Linear(4, 2)

    def forward(self, x):
        v1 = torch.nn.functional.linear(x, self.linear.weight, self.linear.bias)
        v2 = torch.nn.functional.tanh(v1)
        v3 = v2.permute(0, 2, 1)
        return v2 * v3



func = Model().to('cpu')


x = torch.randn(2, 4, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (4) at non-singleton dimension 2

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(2, 4, 2)), FakeTensor(..., size=(2, 2, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([2, 2, 4]); but expected shape should be broadcastable to [2, 4, 2]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''