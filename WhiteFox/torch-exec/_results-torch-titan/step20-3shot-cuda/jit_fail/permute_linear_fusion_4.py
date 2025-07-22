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
        self.input1 = torch.nn.Linear(3, 3)
        self.input2 = torch.nn.Linear(3, 2)

    def forward(self, input):
        v1 = input.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.input1.weight, self.input1.bias)
        x = v2.permute(1, 2, 0)
        v3 = x.contiguous()
        return (torch.relu(v3) + self.input2(v2))




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 3x3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(3,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 2] X [3, 3].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''