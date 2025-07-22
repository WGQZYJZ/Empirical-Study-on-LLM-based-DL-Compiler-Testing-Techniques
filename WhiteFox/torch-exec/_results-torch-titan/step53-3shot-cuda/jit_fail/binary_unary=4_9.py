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
        self.linear = torch.nn.Linear(3, 8)
        self.other = other

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 + self.other)
        v3 = v2.relu()
        return v3



other = 1
func = Model(torch.nn.Parameter(torch.ones(8, 3))).to('cuda')



x = torch.randn(5, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(5, 8)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 3), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([8, 3]); but expected shape should be broadcastable to [5, 8]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''