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
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(t1, input3)
        t4 = torch.mm(input1, input1)
        t3 = t1 + t2 + t4
        return t3



func = Model().to('cpu')


input1 = torch.randn(1, 128)

input2 = torch.randn(768, 128)

input3 = torch.randn(768, 768)

test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x128 and 768x128)

jit:
Failed running call_function <built-in method mm of type object at 0x7a8834596ec0>(*(FakeTensor(..., size=(1, s2)), FakeTensor(..., size=(s0, s1))), **{}):
a and b must have same reduction dim, but got [1, s2] X [s0, s1].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''