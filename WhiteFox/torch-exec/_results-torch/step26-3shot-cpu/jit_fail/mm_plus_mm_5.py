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

    def forward(self, input1, input2, input3, input4):
        t1 = torch.mm(input2, input3)
        t2 = torch.mm(input1, input2)
        return t1 ^ t2



func = Model().to('cpu')


input1 = torch.randn(3, 5)

input2 = torch.randn(3, 2)

input3 = torch.randn(2, 1)

input4 = torch.randn(1, 3)

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x5 and 3x2)

jit:
Failed running call_function <built-in method mm of type object at 0x705e8b796ec0>(*(FakeTensor(..., size=(s3, s4)), FakeTensor(..., size=(s1, s0))), **{}):
a and b must have same reduction dim, but got [s3, s4] X [s1, s0].

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''