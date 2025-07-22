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
        self.scale_factor = 4
        self.dropout_p = 0.5

    def forward(self, x1, x2):
        v1 = x1.matmul(x2.transpose(-2, -1))
        v2 = v1 * self.scale_factor
        v3 = torch.nn.functional.softmax(v2)
        v4 = torch.nn.functional.dropout(v3)
        v5 = v4.matmul(x2)
        return v5


func = Model().to('cpu')


x1 = torch.randn(3, 4)

x2 = torch.randn(4, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x4 and 5x4)

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(3, 4)), FakeTensor(..., size=(5, 4))), **{}):
a and b must have same reduction dim, but got [3, 4] X [5, 4].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''