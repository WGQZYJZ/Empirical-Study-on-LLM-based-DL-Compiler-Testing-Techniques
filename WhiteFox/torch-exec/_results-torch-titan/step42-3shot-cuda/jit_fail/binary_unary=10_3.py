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
        self.linear = torch.nn.Linear(4, 5)

    def forward(self, x1, x2):
        v1 = self.linear(x)
        v2 = (v1 + x2)
        v3 = relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 4)



x2 = torch.randn(1, 5)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., size=(1, 3, 64, 64)),), **{}):
a and b must have same reduction dim, but got [192, 64] X [4, 5].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''