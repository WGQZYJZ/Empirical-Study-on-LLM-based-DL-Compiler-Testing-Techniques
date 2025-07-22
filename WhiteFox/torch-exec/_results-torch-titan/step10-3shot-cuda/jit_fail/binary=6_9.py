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
        self.linear = torch.nn.Linear(8, 8)

    def forward(self, x3):
        v3 = self.linear(x3)
        v40 = torch.randn(16, 8)
        v4 = (v3 - v40)
        return v4



func = Model().to('cuda')



x3 = torch.randn(16, 8)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(16, 8)), FakeTensor(..., size=(16, 8))), **{}):
Unhandled FakeTensor Device Propagation for aten.sub.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''