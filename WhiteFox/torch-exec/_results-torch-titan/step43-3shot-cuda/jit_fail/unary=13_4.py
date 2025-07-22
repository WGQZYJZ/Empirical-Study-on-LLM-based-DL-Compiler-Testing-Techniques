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

    def __init__(self, in_dim, hidden_dim, out_dim):
        super(Model, self).__init__()
        self.i2h = torch.nn.Linear(in_dim, hidden_dim)
        self.h2o = torch.nn.Linear(hidden_dim, out_dim)
        self.s2h = torch.nn.Linear(in_dim, hidden_dim)
        self.s2o = torch.nn.Linear(hidden_dim, out_dim)
        self.h = None

    def forward(self, x):
        h_sig = torch.sigmoid((self.i2h(x) + self.h2o(self.s2h(x))))
        self.h = ((h_sig * self.h) if (self.h is not None) else h_sig)
        o = (self.h + self.h2o(self.s2o(x)))
        return o



in_dim = 1
hidden_dim = 1
out_dim = 1
func = Model(784, 64, 10).to('cuda')



x2 = torch.randn(1, 784)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (10) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 64)), FakeTensor(..., device='cuda:0', size=(1, 10))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([1, 10]); but expected shape should be broadcastable to [1, 64]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''