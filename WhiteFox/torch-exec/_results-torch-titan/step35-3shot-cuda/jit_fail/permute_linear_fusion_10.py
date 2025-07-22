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
        v3 = torch.reshape(x2, (1, 4))
        v4 = torch.nn.functional.avg_pool1d(v3, padding=1)
        v5 = v4.permute(0, 2, 1)
        v6 = torch.nn.functional.relu(v5)
        v7 = torch.reshape(v6, (1, 2))
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
avg_pool1d() missing 1 required positional arguments: "kernel_size"

jit:
Failed running call_function <built-in method avg_pool1d of type object at 0x79fb092699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 4)),), **{'padding': 1}):
avg_pool1d() missing 1 required positional arguments: "kernel_size"

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''