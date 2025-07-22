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

    def forward(self, a):
        x1 = a.permute(0, 2, 1)
        v0 = torch.matmul(x1, x1)
        return v0



func = Model().to('cpu')


x0 = torch.randn(3, 2, 1)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 2] but got: [3, 1].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d18f3d96ec0>(*(FakeTensor(..., size=(3, 1, 2)), FakeTensor(..., size=(3, 1, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 2] but got: [3, 1].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''