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
        v1 = input1 @ input2.transpose(-2, -1)
        v2 = v1 / math.sqrt(v1.size(-1))
        v3 = v2 + input3
        v4 = torch.softmax(v3, dim=-1)
        output = v4 @ input3
        return output


func = Model().to('cpu')


input1 = torch.randn(3, 4, 5)

input2 = torch.randn(5, 6)

input3 = torch.randn(6, 4)

test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x5 and 6x5)

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(3, 4, 5)), FakeTensor(..., size=(6, 5))), **{}):
a and b must have same reduction dim, but got [12, 5] X [6, 5].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''