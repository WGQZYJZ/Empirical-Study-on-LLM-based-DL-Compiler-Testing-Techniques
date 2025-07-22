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

    def forward(self, x):
        v = torch.relu(x)
        v = torch.cat((v, v, v, v), dim=1)
        v = v * v + x * x
        return v.view(-1)



func = Model().to('cuda')


x = torch.randn(5, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (2) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(s0, 4*s1)), FakeTensor(..., device='cuda:0', size=(s0, s1))), **{}):
The size of tensor a (4*s1) must match the size of tensor b (s1) at non-singleton dimension 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''