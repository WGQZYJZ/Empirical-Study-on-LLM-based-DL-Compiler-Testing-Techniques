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
        self.linear1 = torch.nn.Linear(2, 2, device='cuda')
        self.linear2 = torch.nn.Linear(2, 2, device='cuda')
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v2 = torch.nn.functional.relu(x1.cuda())
        v3 = x1 + v2
        v1 = torch.nn.functional.linear(v3, self.linear1.weight, self.linear1.bias)
        a1 = torch.nn.functional.linear(v3, self.linear2.weight, self.linear2.bias)
        v4 = a1.permute(0, 2, 1)
        return v4



func = Model().to('cpu')


x1 = torch.randn(3, 2, 2, device='cuda')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(3, 2, 2)), FakeTensor(..., device='cuda:0', size=(3, 2, 2))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''