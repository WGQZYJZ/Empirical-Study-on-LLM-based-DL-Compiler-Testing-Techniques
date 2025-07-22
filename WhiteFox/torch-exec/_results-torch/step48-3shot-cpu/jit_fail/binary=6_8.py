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
        self.linear = torch.nn.Linear(20, 12)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 - x2
        return (v1, v2)


func = Model().to('cpu')


x1 = torch.randn(4, 20)

x2 = torch.randn(20)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (12) must match the size of tensor b (20) at non-singleton dimension 1

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(s0, 12)), FakeTensor(..., size=(20,))), **{}):
The size of tensor a (12) must match the size of tensor b (20) at non-singleton dimension 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''