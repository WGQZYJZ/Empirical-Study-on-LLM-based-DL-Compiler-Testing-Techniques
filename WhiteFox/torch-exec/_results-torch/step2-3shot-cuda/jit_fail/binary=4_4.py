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
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(100, 300)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + x
        return v2


func = Model().to('cuda')



x = torch.randn(10, 100, dtype=torch.float32, requires_grad=True)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (300) must match the size of tensor b (100) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(s0, 300)), FakeTensor(..., device='cuda:0', size=(s0, 100))), **{}):
The size of tensor a (300) must match the size of tensor b (100) at non-singleton dimension 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''