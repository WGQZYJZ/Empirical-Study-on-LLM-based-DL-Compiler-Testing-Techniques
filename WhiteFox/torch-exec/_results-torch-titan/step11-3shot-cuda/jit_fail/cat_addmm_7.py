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

    def forward(self, x1):
        v1 = torch.tensor([[0.7631, 0.9574, 0.5303], [0.3785, 0.5842, 0.4723], [0.6486, 0.6524, 0.4806]])
        v2 = torch.tensor([[(- 0.2), 0.7019, 1.0966], [0.514, 0.9784, 0.8893], [1.4617, 1.9182, 1.4599]])
        v3 = torch.addmm(x1, v1, v2)
        v4 = v3.clamp(min=0, max=5)
        v5 = torch.cat([v4])
        v6 = (v5 + 0.4202387463864756)
        return v6



func = Model().to('cuda')



x1 = torch.randn(1, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_function <built-in method addmm of type object at 0x7560e48699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 10)), FakeTensor(..., size=(3, 3)), FakeTensor(..., size=(3, 3))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([1, 10]); but expected shape should be broadcastable to [3, 3]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''