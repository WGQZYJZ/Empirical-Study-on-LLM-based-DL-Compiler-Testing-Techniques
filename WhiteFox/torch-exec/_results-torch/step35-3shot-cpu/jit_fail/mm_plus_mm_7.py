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
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input1, input2)
        t3 = torch.mm(input2, input2)
        t4 = torch.mm(input1, input2)
        t5 = torch.mm(input1, input2)
        return t1 + t2 + t3 + t4 + t5



func = Model().to('cpu')


input1 = torch.randn(5, 2)

input2 = torch.randn(2, 4)

test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x4 and 2x4)

jit:
Failed running call_function <built-in method mm of type object at 0x756259196ec0>(*(FakeTensor(..., size=(s0, s1)), FakeTensor(..., size=(s0, s1))), **{}):
a and b must have same reduction dim, but got [s0, s1] X [s0, s1].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''