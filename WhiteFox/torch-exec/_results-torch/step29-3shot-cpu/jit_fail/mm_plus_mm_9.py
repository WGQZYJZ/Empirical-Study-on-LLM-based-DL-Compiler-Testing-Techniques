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
        t1 = torch.mm(input3, input4)
        t2 = torch.mm(input3, input2)
        t3 = torch.mm(input1, input4)
        t4 = torch.mm(input1, input3)
        return t1 + t2 + t3 + t4



func = Model().to('cpu')


input1 = torch.randn(1, 16)

input2 = torch.randn(1, 16)

input3 = torch.randn(1, 16)

input4 = torch.randn(1, 16)

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x16 and 1x16)

jit:
Failed running call_function <built-in method mm of type object at 0x7abc67796ec0>(*(FakeTensor(..., size=(1, s1)), FakeTensor(..., size=(1, s0))), **{}):
a and b must have same reduction dim, but got [1, s1] X [1, s0].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''