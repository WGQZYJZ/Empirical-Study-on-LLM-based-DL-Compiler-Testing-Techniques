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
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, input_tensor: torch.Tensor, **kwargs):
        v2 = input_tensor
        v1 = v2.permute(0, 2, 1)
        v3 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v3




func = Model().to('cuda')



input_tensor = torch.randn(1, 2, 5)


test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x2 and 10x10)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(10, 10), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(10,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [5, 2] X [10, 10].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''