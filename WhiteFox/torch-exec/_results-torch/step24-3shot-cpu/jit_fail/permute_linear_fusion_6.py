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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.relu(v2)
        v3 = torch.max(x2, dim=-1)[0]
        v4 = torch.nn.functional.softmax(torch.nn.functional.softmax(v1, dim=-1)[0].unsqueeze(dim=-1).transpose(0, 1), dim=-1)
        v5 = torch.nn.functional.relu(torch.cat([v4 for i in range(3)], dim=-1)[0])
        v5 = torch.sum(v5, dim=-1)
        v5 = torch.nn.functional.max_pool1d(torch.nn.functional.max_pool1d(v5, 3, 3), 1, 2)
        v6 = torch.sum(torch.nn.functional.pad(v5, (0, 0, 0, 0, 0, 0)))
        return torch.sum(torch.nn.functional.elu(v6.permute([0, 2, 1])))



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
max_pool1d: Expected 2D or 3D (batch mode) tensor with optional 0 dim batch size for input, but got:[2]

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x7e670fb5fd30>(*(FakeTensor(..., size=(2,)), 3, 3), **{}):
max_pool1d: Expected 2D or 3D (batch mode) tensor with optional 0 dim batch size for input, but got:[2]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''