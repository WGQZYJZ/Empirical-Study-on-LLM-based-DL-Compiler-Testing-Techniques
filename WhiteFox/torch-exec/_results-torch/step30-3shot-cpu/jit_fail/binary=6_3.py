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

    def __init__(self, in_features, out_features):
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out_features)

    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2


in_features = 1
out_features = 1
func = Model(16, 16).to('cpu')


x1 = torch.randn(1, 16)

__other = torch.FloatTensor([[[[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]]]])

test_inputs = [x1, __other]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (15) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(1, 16)), FakeTensor(..., size=(1, 1, 1, 15))), **{}):
Attempting to broadcast a dimension of length 15 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 1, 15]); but expected shape should be broadcastable to [1, 1, 1, 16]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''