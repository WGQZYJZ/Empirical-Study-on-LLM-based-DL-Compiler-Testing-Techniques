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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        y = x1
        v1 = torch.nn.functional.linear(y, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1)
        w = v2.size(1)
        h = v2.size(2)
        v3 = v2.contiguous().view(v2.size(0), (w * h))
        v4 = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        w = v4.size(1)
        h = v4.size(2)
        v5 = v4.contiguous().view(v4.size(0), (w * h))
        return v5




func = Model().to('cuda')



x1 = torch.randn(3, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x4 and 2x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(3, 4)), Parameter(FakeTensor(..., device='cuda:0', size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [3, 4] X [2, 2].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''