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



class MyModule(torch.nn.Module):

    def forward(self, x):
        y0 = x.shape[1]
        shape = (1, x.dim())
        y0 = torch.full(shape, 42.0, device=x.device)
        x1 = x.detach()
        y1 = torch.randn(2, 3, 4)
        y1c = y1.to(dtype=torch.int)
        y2 = torch.rand(2, 3, 4, 7, 5)
        ya = (torch.rand((3, 1)) + y2)
        yb = ya.tanh().tanh().tanh()
        z1 = (y1 / y2)
        result1 = torch.mm(z1, y2)
        return result1




func = MyModule().to('cuda')



x = torch.randn(2, 3, 4, 5, 6)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (7) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(3, 1)), FakeTensor(..., size=(2, 3, 4, 7, 5))), **{}):
Attempting to broadcast a dimension of length 7 at -2! Mismatching argument at index 1 had torch.Size([2, 3, 4, 7, 5]); but expected shape should be broadcastable to [1, 1, 1, 3, 5]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''