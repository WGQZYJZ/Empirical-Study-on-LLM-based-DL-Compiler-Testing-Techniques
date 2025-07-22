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
        self.linear1 = torch.nn.Linear(3, 5)
        self.linear2 = torch.nn.Linear(5, 3)
        self.linear3 = torch.nn.Linear(8, 9)
        self.linear4 = torch.nn.Linear(9, 4)

    def forward(self, x1):
        v1 = torch.cos(x1)
        v2 = torch.nn.functional.linear(v1, self.linear4.weight, self.linear4.bias)
        v3 = v2.permute(0, 2, 1)
        v4 = torch.nn.functional.linear(v3, self.linear3.weight, self.linear3.bias)
        v5 = torch.sigmoid(v4)
        v6 = v1.view(1, 480)
        v7 = torch.sigmoid(torch.nn.functional.linear(v6, self.linear1.weight, self.linear1.bias))
        v8 = torch.max(v5, dim=(- 1), keepdim=False)[0]
        v9 = torch.nn.functional.linear(v8, self.linear2.weight, self.linear2.bias)
        return v9




func = Model().to('cuda')



x1 = torch.randn(6, 480)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x480 and 9x4)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(6, 480)), Parameter(FakeTensor(..., device='cuda:0', size=(4, 9), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(4,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [6, 480] X [9, 4].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''