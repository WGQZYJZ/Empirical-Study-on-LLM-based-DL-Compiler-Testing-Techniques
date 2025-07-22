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

    def forward(self, x1, x2):
        v1 = x1.transpose(0, 2)
        v2 = x2.permute(0, 2, 1)
        v3 = torch.matmul(v2, v1)
        v4 = torch.matmul(v1, v3)
        v5 = v4 * v2
        v6 = v5 - v1
        v7 = v4 + v6
        return (v4, v7)



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

x2 = torch.randn(1, 2, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 1] but got: [2, 2].

jit:
Failed running call_function <built-in method matmul of type object at 0x737298596ec0>(*(FakeTensor(..., size=(s0, 2, 1)), FakeTensor(..., size=(s0, 2, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0, 1] but got: [s0, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''