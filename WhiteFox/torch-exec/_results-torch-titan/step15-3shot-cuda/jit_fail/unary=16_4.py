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
        self.linear = torch.nn.Linear(8, 4)

    def forward(self, x2):
        v1 = self.linear(x1)
        v2 = torch.relu(v1)
        return v2



func = Model().to('cuda')



x2 = torch.randn(1, 8)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., size=(1, 16)),), **{}):
a and b must have same reduction dim, but got [1, 16] X [8, 4].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''