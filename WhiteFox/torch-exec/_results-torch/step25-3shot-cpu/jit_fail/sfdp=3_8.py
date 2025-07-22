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

    def forward(self, x1, x2, x3, x4):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1.mul(0.5)
        v3 = v1.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.1)
        v5 = torch.matmul(v4, x3)
        v6 = v5 + x4
        return v6


func = Model().to('cpu')


x1 = torch.randn(1, 10, 20)

x2 = torch.randn(1, 20, 5)

x3 = torch.randn(1, 5, 10)

x4 = torch.randn(1, 10, 30)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 20] but got: [1, 5].

jit:
Failed running call_function <built-in method matmul of type object at 0x77f619996ec0>(*(FakeTensor(..., size=(1, 10, 20)), FakeTensor(..., size=(1, 5, 20))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 20] but got: [1, 5].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''