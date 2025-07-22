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
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        v3 = torch.matmul(v1, x2)
        v4 = x2.permute(0, 2, 1)
        v5 = torch.matmul(v3, v1)
        return (v3, v4, v5)



func = Model().to('cpu')


x1 = torch.randn(4, 2, 2)

x2 = torch.randn(4, 2, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 5] but got: [4, 2].

jit:
Failed running call_function <built-in method matmul of type object at 0x7dea82396ec0>(*(FakeTensor(..., size=(4, 2, 5)), FakeTensor(..., size=(4, 2, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 5] but got: [4, 2].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''