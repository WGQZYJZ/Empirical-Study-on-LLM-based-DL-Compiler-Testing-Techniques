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
        self.linear = torch.nn.Linear(10, 20)

    def forward(self, x1, w1):
        v1 = self.linear(x1)
        v2 = torch.nn.functional.linear(v1, w1)
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 10)

w1 = torch.randn(20, 10)

test_inputs = [x1, w1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x20 and 10x20)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 20)), FakeTensor(..., size=(20, 10))), **{}):
a and b must have same reduction dim, but got [1, 20] X [10, 20].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''