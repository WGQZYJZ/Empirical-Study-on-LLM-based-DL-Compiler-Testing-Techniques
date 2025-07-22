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

    def forward(self, input1, input2, input3, input4, input5):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3 = torch.mm(input5, input1)
        return t1 + t2 + t3



func = Model().to('cpu')


input1 = torch.randn(1, 12)

input2 = torch.randn(12, 8)

input3 = torch.randn(11, 12)

input4 = torch.randn(126, 128)

input5 = torch.randn(128, 1)

test_inputs = [input1, input2, input3, input4, input5]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (11x12 and 126x128)

jit:
Failed running call_function <built-in method mm of type object at 0x7776bf796ec0>(*(FakeTensor(..., size=(s5, s6)), FakeTensor(..., size=(s3, s4))), **{}):
a and b must have same reduction dim, but got [s5, s6] X [s3, s4].

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''