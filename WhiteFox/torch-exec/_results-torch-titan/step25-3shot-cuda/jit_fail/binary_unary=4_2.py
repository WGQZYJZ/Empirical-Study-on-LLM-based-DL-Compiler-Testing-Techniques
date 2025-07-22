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
        self.linear = torch.nn.Linear(4, 3)

    def forward(self, x1, other=torch.randn(1, 4).to(torch.float32), other_scalar=4.0):
        v1 = self.linear(x1)
        v2 = (v1 + other)
        v3 = relu(v2)
        v3_add = (v3 + other_scalar)
        return v4_add



func = Model().to('cuda')




x1 = torch.randn(1, 4).to(torch.float32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 3)), FakeTensor(..., size=(1, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 4]); but expected shape should be broadcastable to [1, 3]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''