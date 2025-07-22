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
        self.linear = torch.nn.Linear(3, 2)
        self.linear_2 = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(1, 2, 0)
        result = self.linear_2.forward(v2)
        return result




func = Model().to('cuda')



x1 = torch.randn(1, 2, 3, device='cpu')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x1 and 3x2)

jit:
Failed running call_method forward(*(Linear(in_features=3, out_features=2, bias=True), FakeTensor(..., device='cuda:0', size=(2, 2, 1))), **{}):
a and b must have same reduction dim, but got [4, 1] X [3, 2].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''