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
        v1 = torch.unsqueeze(x1, 1)
        v2 = torch.reshape(v1, (-1, 3))
        v3 = torch.matmul(v2, torch.ones(3, 1))
        v4 = torch.reshape(v3, (1, 2, 2))
        return torch.squeeze(v4)



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 3]' is invalid for input of size 4

jit:
Failed running call_function <built-in method reshape of type object at 0x7bf32d596ec0>(*(FakeTensor(..., size=(1, 1, 2, 2)), (-1, 3)), **{}):
shape '[-1, 3]' is invalid for input of size 4

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''