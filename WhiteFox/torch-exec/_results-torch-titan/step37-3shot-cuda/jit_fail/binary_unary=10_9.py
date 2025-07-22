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
        self.linear = torch.nn.Linear(30, 20)

    def forward(self, x1, x2, x3):
        v1 = self.linear(x1)
        v2 = (v1 + x2)
        v3 = torch.relu(v2)
        v4 = (v3 + x3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 30)



x2 = torch.randn(1, 30)



x3 = torch.randn(1, 30)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (20) must match the size of tensor b (30) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 20)), FakeTensor(..., device='cuda:0', size=(1, 30))), **{}):
Attempting to broadcast a dimension of length 30 at -1! Mismatching argument at index 1 had torch.Size([1, 30]); but expected shape should be broadcastable to [1, 20]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''