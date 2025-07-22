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

    def __init__(self, in_features_0: int, out_features_0: int, in_features_1: int):
        super().__init__()
        self.linear = torch.nn.Linear(in_features_0, out_features_0)
        self.other = torch.nn.Parameter(torch.ones(1, in_features_1))

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.other)
        v3 = torch.relu(v2)
        return v3



in_features_0 = 1
out_features_0 = 1
in_features_1 = 1
func = Model(11, 13, 17).to('cuda')



x1 = torch.randn(13, 11)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (13) must match the size of tensor b (17) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(13, 13)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 17), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 17 at -1! Mismatching argument at index 1 had torch.Size([1, 17]); but expected shape should be broadcastable to [13, 13]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''