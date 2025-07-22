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
        self.linear = torch.nn.Linear(12, 24, bias=False)
        self.bias = torch.nn.Parameter(torch.zeros(1, 24, dtype=torch.float32))

    def forward(self, x1):
        w1 = self.linear.weight.to(x1.device)
        v2 = torch.matmul(x1, w1)
        v3 = v2 + self.bias
        v4 = torch.nn.functional.relu(v3)
        return v4


func = Model().to('cpu')



x1 = torch.randn(1, 12, dtype=torch.float32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x12 and 24x12)

jit:
Failed running call_function <built-in method matmul of type object at 0x7b4739f96ec0>(*(FakeTensor(..., size=(1, 12)), Parameter(FakeTensor(..., size=(24, 12), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 12] X [24, 12].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''