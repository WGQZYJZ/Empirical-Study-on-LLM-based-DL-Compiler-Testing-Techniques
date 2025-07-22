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

    def __init__(self):
        super().__init__()

    def forward(self, input1, input2, input3):
        v1 = torch.matmul(input1, input2.transpose(-2, -1))
        v2 = v1.mul(10)
        v3 = x3.softmax(-1)
        v4 = torch.nn.functional.dropout(v3, p=0.1)
        return v4.matmul(input3)


func = Model().to('cpu')


input1 = torch.randn(50, 64)

input2 = torch.randn(64, 80)

input3 = torch.randn(80, 10)

test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (50x64 and 80x64)

jit:
Failed running call_function <built-in method matmul of type object at 0x7ad738996ec0>(*(FakeTensor(..., size=(50, 64)), FakeTensor(..., size=(80, 64))), **{}):
a and b must have same reduction dim, but got [50, 64] X [80, 64].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''