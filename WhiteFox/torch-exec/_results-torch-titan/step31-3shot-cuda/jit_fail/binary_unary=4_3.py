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
        self.weight = torch.randn(1000, 512)
        self.bias = torch.randn(512)

    def forward(self, x1, other=None):
        v1 = torch.matmul(x1, self.weight.t())
        v2 = (v1 + other)
        v3 = torch.nn.functional.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 1000)



other = torch.randn(1, 512)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1000 and 512x1000)

jit:
Failed running call_function <built-in method matmul of type object at 0x7d31142699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1000)), FakeTensor(..., device='cuda:0', size=(512, 1000))), **{}):
a and b must have same reduction dim, but got [1, 1000] X [512, 1000].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''