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
        v1 = torch.randn(4, 2, 3)
        v2 = torch.randn(4, 2, 5)
        v3 = torch.randn(4, 2, 5)
        v4 = torch.bmm(v1, v1)
        v5 = torch.matmul(x2, x2)
        v6 = torch.bmm(v2, v2)
        v7 = torch.matmul(v6, v6)
        v8 = torch.bmm(v4, v2)
        return (v1, v2, v3, v4, v5, v6, v7, v8)



func = Model().to('cpu')


x1 = torch.randn(4, 2, 2)

x2 = torch.randn(4, 2, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 3] but got: [4, 2].

jit:
Failed running call_function <built-in method bmm of type object at 0x7dea82396ec0>(*(FakeTensor(..., size=(4, 2, 3)), FakeTensor(..., size=(4, 2, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 3] but got: [4, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''