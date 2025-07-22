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
        tt = torch.mm(input1, input4)
        t1 = torch.mm(input2, input4)
        t2 = torch.mm(input3, input4)
        t3 = t1 + t2 + tt
        return t3



func = Model().to('cpu')


input1 = torch.randn(4, 3)

input2 = torch.randn(3, 2)

input3 = torch.randn(2, 4)

input4 = torch.randn(4, 3)

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x3 and 4x3)

jit:
Failed running call_function <built-in method mm of type object at 0x7720c2796ec0>(*(FakeTensor(..., size=(s0, s1)), FakeTensor(..., size=(4, 3))), **{}):
a and b must have same reduction dim, but got [s0, s1] X [4, 3].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''