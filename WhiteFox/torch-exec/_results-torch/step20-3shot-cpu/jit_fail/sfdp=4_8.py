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

    def forward(self, x1, x2, x3):
        v1 = torch.matmul(x1, x2)
        v2 = v1 / math.sqrt(v1.size(-1))
        v3 = v2 + x3
        v4 = torch.softmax(v3, dim=-1)
        v5 = torch.matmul(v4, x2)
        return v5


func = Model().to('cpu')


x1 = torch.randn(1, 32, 100)

x2 = torch.randn(1, 32, 100)

x3 = torch.rand(1, 100, 100)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 100] but got: [1, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x789134b96ec0>(*(FakeTensor(..., size=(1, 32, 100)), FakeTensor(..., size=(1, 32, 100))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 100] but got: [1, 32].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''