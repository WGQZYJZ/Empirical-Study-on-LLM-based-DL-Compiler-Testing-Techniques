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
        y = torch.cat((x, x), dim=-1).view(x.shape[0], -1)
        x = x.view(x.shape[0], -1) + y
        return x.tanh() if y.shape == (1, 2) else y.tanh()



func = Model().to('cpu')


x = torch.randn(2, 3, 3, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (36) must match the size of tensor b (72) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, s1*s2*s3)), FakeTensor(..., size=(s0, 2*s1*s2*s3))), **{}):
The size of tensor a (s1*s2*s3) must match the size of tensor b (2*s1*s2*s3) at non-singleton dimension 1)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''