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
        self.linear1 = torch.nn.Linear(1, 4)
        self.conv1 = torch.nn.Conv2d(1, 2, 2)
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(self.conv1(x1), self.linear1.weight, self.linear1.bias)
        return self.linear2(v1)




func = Model().to('cuda')



x1 = torch.randn(2, 1, 4, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x2 and 1x4)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(2, 2, 3, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(4, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(4,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [12, 2] X [1, 4].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''