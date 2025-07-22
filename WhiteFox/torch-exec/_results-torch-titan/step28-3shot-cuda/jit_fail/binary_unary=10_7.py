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

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
        self.other = other

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.other)
        v3 = torch.nn.functional.ReLU()(v2)
        return v3



other = 1
func = Model(torch.randn(10, 5)).to('cuda')



x1 = torch.randn(1, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (5) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 10)), FakeTensor(..., device='cuda:0', size=(10, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([10, 5]); but expected shape should be broadcastable to [1, 10]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''