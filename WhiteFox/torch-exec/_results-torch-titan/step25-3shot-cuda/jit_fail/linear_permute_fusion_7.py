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
        x2 = torch.unsqueeze(x1, 1)
        x3 = torch.transpose(x2, 1, (- 1))
        x4 = torch.squeeze(x1, (- 2))
        x5 = torch.matmul(x3, x4)
        x6 = (x3 * x4)
        x7 = (x3 + x4)
        v1 = torch.nn.functional.linear(x5, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x1 and 2x2)

jit:
Failed running call_function <built-in method matmul of type object at 0x78c287e699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2, 1)), FakeTensor(..., device='cuda:0', size=(2, 2))), **{}):
a and b must have same reduction dim, but got [4, 1] X [2, 2].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''