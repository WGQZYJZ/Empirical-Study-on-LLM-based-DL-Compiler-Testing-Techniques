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

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()

    def forward(self, input1, input2, input3, input4):
        t1 = torch.mm(input3, input4)
        t2 = torch.mm(input1, input4)
        t2 = torch.mm(input1, input2)
        t3 = t1 + t2
        return t3



func = Model().to('cpu')


input1 = torch.randn(8, 8)

input2 = torch.randn(16, 8)

input3 = torch.randn(2, 8)

input4 = torch.randn(8, 2)

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x8 and 16x8)

jit:
Failed running call_function <built-in method mm of type object at 0x7cdf65d96ec0>(*(FakeTensor(..., size=(8, 8)), FakeTensor(..., size=(16, 8))), **{}):
a and b must have same reduction dim, but got [8, 8] X [16, 8].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''