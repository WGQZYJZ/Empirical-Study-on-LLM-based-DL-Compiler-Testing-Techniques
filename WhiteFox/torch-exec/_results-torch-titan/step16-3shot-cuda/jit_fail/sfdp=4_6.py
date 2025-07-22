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

    def forward(self, x1, x2):
        v1 = (x1 @ x2.transpose((- 2), (- 1)))
        v1 = (v1 / math.sqrt(v1.size((- 1))))
        v1 = (v1 + (torch.rand(v1.shape) + 1))
        v2 = torch.softmax(v1, dim=(- 1))
        v3 = (v2 @ x2)
        return v3



func = Model().to('cuda')



d1 = 10


x1 = torch.randn(1, d1, 8)



d2 = 6


x2 = torch.randn(1, d2, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 10, 6)), FakeTensor(..., size=(1, 10, 6))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''