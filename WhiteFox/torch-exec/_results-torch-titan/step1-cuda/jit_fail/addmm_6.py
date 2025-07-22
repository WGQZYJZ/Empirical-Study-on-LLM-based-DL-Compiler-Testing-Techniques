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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1.size()
        v3 = torch.FloatTensor(3, 3).uniform_((- 0.5), 1.0)
        v4 = torch.matmul(v1, v3)
        return (v2, {'inp': v4})



func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method matmul of type object at 0x78d9c36699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)), FakeTensor(..., size=(3, 3))), **{}):
a and b must have same reduction dim, but got [512, 64] X [3, 3].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''