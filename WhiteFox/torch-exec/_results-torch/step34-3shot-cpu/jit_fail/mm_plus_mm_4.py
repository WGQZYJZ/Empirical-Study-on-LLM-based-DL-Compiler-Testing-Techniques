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

    def forward(self, input1, weights):
        t1 = torch.mm(input1, weights)
        t2 = torch.mm(t1, weights.t())
        return t2.t()



func = Model().to('cpu')


input1 = torch.randn(4, 4)

weights = torch.randn(100, 1000)

test_inputs = [input1, weights]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x4 and 100x1000)

jit:
Failed running call_function <built-in method mm of type object at 0x7a8834596ec0>(*(FakeTensor(..., size=(s0, s1)), FakeTensor(..., size=(100, 1000))), **{}):
a and b must have same reduction dim, but got [s0, s1] X [100, 1000].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''