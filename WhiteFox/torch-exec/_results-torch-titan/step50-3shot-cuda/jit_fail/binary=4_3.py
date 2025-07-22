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
        self.linear1 = torch.nn.Linear(64, 32, bias=True)
        self.linear2 = torch.nn.Linear(32, 16, bias=False)

    def forward(self, x, other):
        v1 = self.linear1(x)
        v2 = (v1 + other)
        v3 = self.linear2(v2)
        return v2



func = Model().to('cuda')



x = torch.randn(2, 64)



v6 = torch.randn(2, 16)


test_inputs = [x, v6]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(2, 32)), FakeTensor(..., device='cuda:0', size=(2, 16))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([2, 16]); but expected shape should be broadcastable to [2, 32]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''