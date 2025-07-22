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

    def forward(self, input1, input2, input3):
        t1 = torch.mm(input1, input3)
        t2 = torch.mm(input2, input3)
        t3 = torch.tanh(t1) + t2 + torch.mm(input1, input2)
        t4 = t1 + 2.0 * t2 + 3.0 * torch.mm(input3, input4)
        t5 = t3 * t4
        return t5.sum()



func = Model().to('cpu')


input1 = torch.randn(2, 5)

input2 = torch.randn(2, 5)

input3 = torch.randn(5, 2)

test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x5 and 2x5)

jit:
Failed running call_function <built-in method mm of type object at 0x7ba1b1196ec0>(*(FakeTensor(..., size=(s2, s0)), FakeTensor(..., size=(s2, s0))), **{}):
a and b must have same reduction dim, but got [s2, s0] X [s2, s0].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''