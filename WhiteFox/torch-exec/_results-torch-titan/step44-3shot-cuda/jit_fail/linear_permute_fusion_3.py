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

    def forward(self, x0):
        v0 = torch.nn.functional.linear(x0, torch.tensor([[1.0]], device='cuda', dtype=torch.float16), bias=None)
        v1 = v0.permute(0, 2, 1)
        v2 = v1.bool()
        return v2




func = Model().to('cuda')




x0 = torch.randn(2, 2, 2, dtype=torch.float32)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x2 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(2, 2, 2)), FakeTensor(..., device='cuda:0', size=(1, 1), dtype=torch.float16)), **{'bias': None}):
a and b must have same reduction dim, but got [4, 2] X [1, 1].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''