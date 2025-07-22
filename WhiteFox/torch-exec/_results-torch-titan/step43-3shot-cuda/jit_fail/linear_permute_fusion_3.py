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
        self.linear = torch.nn.Linear(6, 6)

    def forward(self, x0):
        v0 = torch.nn.functional.linear(x0, self.linear.weight, self.linear.bias)
        v1 = v0.permute(2, 0, 1)
        v2 = v1.permute(0, 2, 1)
        v3 = v1.permute(2, 0, 1)
        v4 = v1.permute(1, 2, 0)
        return (((v0 + v2) + v3) + v4)




func = Model().to('cuda')



x0 = torch.randn(1, 2, 3)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 6x6)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3)), Parameter(FakeTensor(..., device='cuda:0', size=(6, 6), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(6,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 3] X [6, 6].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''