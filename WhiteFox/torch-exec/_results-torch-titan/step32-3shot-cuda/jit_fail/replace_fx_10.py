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

    def forward(self, x):
        y1 = torch.randn(1)
        y2 = torch.randn(1)
        m = torch.nn.Dropout(0.3)
        y3 = m(y1)
        y4 = (y3 * 2)
        y5 = (y2 + y4)
        x1 = torch.nn.functional.dropout(x, p=0.1)
        z1 = (x1 * 5)
        z2 = (z1 + y5)
        return z2




func = model().to('cuda')



x1 = torch.randn(1, requires_grad=True)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1,)), FakeTensor(..., size=(1,))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''