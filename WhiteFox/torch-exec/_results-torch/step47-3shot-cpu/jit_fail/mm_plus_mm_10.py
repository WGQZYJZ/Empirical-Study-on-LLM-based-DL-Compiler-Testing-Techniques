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

    def forward(self, input1, input2):
        a = torch.mm(input1, input1)
        b = torch.mm(input2, input2)
        c = torch.mm(input2, input1)
        return a * b - c



func = Model().to('cpu')


input1 = torch.randn(7, 4)

input2 = torch.randn(7, 4)

test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (7x4 and 7x4)

jit:
Failed running call_function <built-in method mm of type object at 0x73c654b96ec0>(*(FakeTensor(..., size=(7, 4)), FakeTensor(..., size=(7, 4))), **{}):
a and b must have same reduction dim, but got [7, 4] X [7, 4].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''