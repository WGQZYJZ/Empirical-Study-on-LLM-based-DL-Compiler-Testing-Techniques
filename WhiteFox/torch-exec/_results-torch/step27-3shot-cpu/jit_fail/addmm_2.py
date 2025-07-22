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

    def forward(self, x1):
        return x1 + torch.randn_like(x1) @ torch.randn(5, 5)



func = Model().to('cpu')


x1 = torch.randn(3, 3, requires_grad=True)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x3 and 5x5)

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(3, 3)), FakeTensor(..., size=(5, 5))), **{}):
a and b must have same reduction dim, but got [3, 3] X [5, 5].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''