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

    def forward(self, inputs1, input2, input3, input4, input5):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3 = torch.mm(input1, input4)
        t4 = torch.mm(input3, input2)
        t5 = torch.mm(input5, input3)
        t6 = torch.mm(input5, input4)
        t7 = torch.mm(input5, input2)
        return t1 + t2 + t3 + t4 + t5 + t6 + t7



func = Model().to('cpu')


inputs1 = torch.randn(2, 2)

input2 = torch.randn(2, 2)

input3 = torch.randn(2, 2)

input4 = torch.randn(2, 2)

input5 = torch.randn(2, 2)

test_inputs = [inputs1, input2, input3, input4, input5]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x3 and 2x2)

jit:
Failed running call_function <built-in method mm of type object at 0x756259196ec0>(*(FakeTensor(..., size=(3, 3), requires_grad=True), FakeTensor(..., size=(s0, s1))), **{}):
a and b must have same reduction dim, but got [3, 3] X [s0, s1].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''