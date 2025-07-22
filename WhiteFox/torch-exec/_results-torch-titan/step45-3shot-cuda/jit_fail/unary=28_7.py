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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, torch.ones([2, 3], dtype=torch.float32), torch.zeros([2, 3], dtype=torch.float32))
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3



min_value = 1
max_value = 1

func = Model(min_value, max_value).to('cuda')



x1 = torch.randn(3, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(3, 2)), FakeTensor(..., size=(2, 3)), FakeTensor(..., size=(2, 3))), **{}):
a and b must have same reduction dim, but got [3, 2] X [3, 2].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''