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
        self.linear = torch.nn.Linear(in_features=100, out_features=3000, bias=True)

    def forward(self, tensor):
        v1 = self.linear(tensor)
        v2 = torch.zeros((3, 50, 100))
        v3 = v1 + v2
        v4 = torch.relu(v3)
        return v4


func = Model().to('cpu')


tensor = torch.randn(1, 100)

test_inputs = [tensor]

# JIT_FAIL
'''
direct:
The size of tensor a (3000) must match the size of tensor b (100) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 3000)), FakeTensor(..., size=(3, 50, 100))), **{}):
Attempting to broadcast a dimension of length 100 at -1! Mismatching argument at index 1 had torch.Size([3, 50, 100]); but expected shape should be broadcastable to [1, 1, 3000]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''