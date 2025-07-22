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
        v1 = x1 @ x2.transpose(-2, -1)
        v2 = v1 / math.sqrt(x1.size(-1))
        v3 = v2 + 0
        v4 = torch.softmax(v3, -1)
        v5 = v4 @ x2
        return v5


func = Model().to('cpu')


x1 = torch.randn(2, 3, 32, 64)

x2 = torch.randn(2, 4, 32, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(2, 3, 32, 64)), FakeTensor(..., size=(2, 4, 64, 32))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''