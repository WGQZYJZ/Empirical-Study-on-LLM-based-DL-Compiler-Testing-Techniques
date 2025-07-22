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

    def forward(self, x, y):
        z1 = torch.nn.functional.glu(x, dim=-1) + torch.nn.functional.glu(y, dim=-2)
        w1 = torch.nn.functional.gelu(z1)
        p1 = torch.nn.functional.glu(x) + torch.nn.functional.glu(w1)
        return torch.nn.functional.gelu(p1)



func = Model().to('cpu')


x = torch.randn(10, 20)

y = torch.randn(10, 20)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (20) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(10, 10)), FakeTensor(..., size=(5, 20))), **{}):
Attempting to broadcast a dimension of length 20 at -1! Mismatching argument at index 1 had torch.Size([5, 20]); but expected shape should be broadcastable to [10, 10]

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''