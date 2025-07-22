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
        x2 = torch.nn.functional.linear(x1, torch.randn(4), torch.tensor([0.0, 1.0, 2.0, 3.0]))
        v1 = x1.permute(1, 2, 0)
        x2 = (x2 + v1)
        x2 = torch.nn.functional.relu(x2)
        return x2




func = Model().to('cuda')



x1 = torch.randn(5, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(5, 2, 2)), FakeTensor(..., size=(4,)), FakeTensor(..., size=(4,))), **{}):
b must be 2D

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''