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
        self.linear0 = torch.nn.Linear(32, 32)
        self.linear1 = torch.nn.Linear(32, 32)

    def forward(self, x1):
        mat0 = self.linear0(x1)
        mat1 = self.linear1(x1)
        m0 = (mat0.matmul(mat1.transpose((- 2), (- 1))) / math.sqrt(mat0.size((- 1))))
        m1 = (m0 + (torch.ones(32, 32) * 100000))
        w12 = torch.softmax(m1, dim=(- 1))
        o12 = w12.matmul(mat0)
        return o12



func = Model().to('cuda')



x1 = torch.randn(32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(32, 32)), FakeTensor(..., size=(32, 32))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''