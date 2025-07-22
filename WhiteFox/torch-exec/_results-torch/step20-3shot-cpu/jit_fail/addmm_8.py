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

    def forward(self, x1, x2, inp1, inp2):
        v1 = torch.mm(x2, x1)
        v2 = inp1
        v2 = v1 + v2
        v2 = v2 + inp2
        return v2



func = Model().to('cpu')


x1 = torch.randn(3, 3)

x2 = torch.randn(5, 3)

inp1 = torch.randn(5, 3, 3)

inp2 = torch.randn(3, 3, 5)

test_inputs = [x1, x2, inp1, inp2]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s1, 3)), FakeTensor(..., size=(5, 3, 3))), **{}):
The size of tensor a (s1) must match the size of tensor b (3) at non-singleton dimension 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''