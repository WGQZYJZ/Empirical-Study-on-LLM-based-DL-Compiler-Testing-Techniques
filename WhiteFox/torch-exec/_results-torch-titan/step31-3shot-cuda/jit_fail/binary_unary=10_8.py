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
        self.lin = torch.nn.Linear(10, 6)

    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = (v1 + torch.sinh(x1))
        v3 = torch.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(2, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (10) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(2, 6)), FakeTensor(..., device='cuda:0', size=(2, 10))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([2, 10]); but expected shape should be broadcastable to [2, 6]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''