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
        self.fc = torch.nn.Linear(80, 40)

    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 + x1
        return v2


func = Model().to('cpu')


x1 = torch.randn(2, 80)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (40) must match the size of tensor b (80) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, 40)), FakeTensor(..., size=(s0, 80))), **{}):
The size of tensor a (40) must match the size of tensor b (80) at non-singleton dimension 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''