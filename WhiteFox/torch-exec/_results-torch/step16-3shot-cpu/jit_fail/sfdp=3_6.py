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

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 * 10000.0
        v3 = nn.functional.softmax(v2, -1)
        v4 = nn.functional.dropout(v3, 0.2)
        v5 = v4.matmul(x2)
        return v5


func = Model().to('cpu')


x1 = torch.randn(1, 8, 128, 128)

x2 = torch.randn(1, 512, 16, 16)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (512) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7751bd996ec0>(*(FakeTensor(..., size=(1, 8, 128, 128)), FakeTensor(..., size=(1, 512, 16, 16))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''