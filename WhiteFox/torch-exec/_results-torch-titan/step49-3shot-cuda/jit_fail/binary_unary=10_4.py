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

    def __init__(self, dim_in, dim_hidden, dim_out):
        super().__init__()
        self.linear1 = torch.nn.Linear(dim_in, dim_hidden)
        self.linear2 = torch.nn.Linear(dim_hidden, dim_out)

    def forward(self, t):
        v = self.linear1(t)
        v = (v + t)
        v = torch.relu(v)
        v = self.linear2(v)
        return v



dim_in = 1
dim_hidden = 1
dim_out = 1
func = Model(5, 100, 1).to('cuda')



x = torch.randn(1, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (100) must match the size of tensor b (5) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 100)), FakeTensor(..., device='cuda:0', size=(1, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([1, 5]); but expected shape should be broadcastable to [1, 100]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''