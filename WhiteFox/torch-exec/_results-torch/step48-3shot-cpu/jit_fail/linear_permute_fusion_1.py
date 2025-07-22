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
        self.linear = torch.nn.Linear(4, 2)

    def forward(self, input_tensor):
        t1 = torch.nn.functional.linear(input_tensor, self.linear.weight, self.linear.bias)
        t1_perm = t1.permute(0, 2, 1, 3)
        return t1_perm



func = Model().to('cpu')


input_tensor = torch.randn(1, 2, 2, 2)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x2 and 4x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 2, 2)), Parameter(FakeTensor(..., size=(2, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4, 2] X [4, 2].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''