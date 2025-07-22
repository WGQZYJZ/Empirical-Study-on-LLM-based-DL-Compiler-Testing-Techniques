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
        self.linear = torch.nn.Linear(44, 101)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 3, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2




func = Model().to('cuda')



x1 = torch.randn(2, 3, 44, 81)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (7128x3 and 44x101)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(2, 44, 81, 3)), Parameter(FakeTensor(..., device='cuda:0', size=(101, 44), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(101,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [7128, 3] X [44, 101].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''