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
        self.linear = torch.nn.Linear(in_features=5, out_features=8)

    def forward(self, input_1, v1, v2):
        v3 = (torch.matmul(input_1, self.linear.weight) + self.linear.bias)
        v4 = torch.clamp(v3, min=v1, max=v2)
        return v4



func = Model().to('cuda')



x1 = torch.randn(5)

input_1 = 1
v1 = 1

test_inputs = [x1, input_1, v1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x5 and 8x5)

jit:
Failed running call_function <built-in method matmul of type object at 0x7b4c52a699e0>(*(FakeTensor(..., device='cuda:0', size=(5,)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 5), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 5] X [8, 5].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''