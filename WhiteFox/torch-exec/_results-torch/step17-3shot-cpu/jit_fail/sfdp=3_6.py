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
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 * 10
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = self.dropout(v3)
        output = v4.matmul(x2)
        return output


func = Model().to('cpu')


x1 = torch.randn(2, 3)

x2 = torch.randn(5, 9)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 9x5)

jit:
Failed running call_function <built-in method matmul of type object at 0x76edc6b96ec0>(*(FakeTensor(..., size=(2, 3)), FakeTensor(..., size=(9, 5))), **{}):
a and b must have same reduction dim, but got [2, 3] X [9, 5].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''