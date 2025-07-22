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
        self.linear = torch.nn.Linear(32, 32)

    def forward(self, x1):
        y = x1
        v5 = torch.nn.functional.linear(y, self.linear.weight, self.linear.bias)
        v4 = v5.permute(0, 2, 1)
        v3 = torch.nn.functional.batch_norm(v4, None, None, self.layernorm.weight, self.layernorm.bias, True, 0.019999999552965164, 1.0000000000000003e-05).contiguous()
        v1 = torch.nn.functional.layer_norm(v3, v3.size(1), self.layernorm.weight, self.layernorm.bias, 1e-05, True).contiguous()
        v2 = v1.permute(0, 2, 1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(3, 2, 2, device='cpu')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x2 and 32x32)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(3, 2, 2)), Parameter(FakeTensor(..., size=(32, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [6, 2] X [32, 32].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''