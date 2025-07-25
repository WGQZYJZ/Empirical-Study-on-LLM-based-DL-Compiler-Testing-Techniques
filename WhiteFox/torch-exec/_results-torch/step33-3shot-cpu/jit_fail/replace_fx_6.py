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

class model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.parameter0 = torch.nn.Parameter(torch.tensor((-0.0535, -1.3267, -1.1838, 1.0735), dtype=torch.float32))

    def forward(self, x1):
        x2 = torch.nn.functional.dropout(x1)
        x3 = x1 + 1
        x4 = self.parameter0 - x3
        return x4



func = model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 2

jit:
Failed running call_function <built-in function sub>(*(Parameter(FakeTensor(..., size=(4,), requires_grad=True)), FakeTensor(..., size=(1, s0, s1))), **{}):
The size of tensor a (4) must match the size of tensor b (s1) at non-singleton dimension 2)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''