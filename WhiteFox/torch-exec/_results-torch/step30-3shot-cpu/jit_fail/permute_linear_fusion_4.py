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

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v3 = torch.matmul(v1, v1)
        v4 = v3.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v4, v4, v4)
        return v2



func = Model().to('cpu')


x1 = torch.randn(3, 18, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 18] but got: [3, 10].

jit:
Failed running call_function <built-in method matmul of type object at 0x73dbbe996ec0>(*(FakeTensor(..., size=(3, 10, 18)), FakeTensor(..., size=(3, 10, 18))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 18] but got: [3, 10].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''