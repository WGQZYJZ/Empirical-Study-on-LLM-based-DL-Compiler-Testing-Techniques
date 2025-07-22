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
        w1 = torch.rand(1, 1, 1)
        y = (x * w1)
        w2 = torch.rand(1, 1, 2, 3)
        x_bchw = ((x + y) + w2)
        return x_bchw




func = Model().to('cuda')



x = torch.randn(1, 1, 2, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 2, 3)), FakeTensor(..., size=(1, 1, 1))), **{}):
Unhandled FakeTensor Device Propagation for aten.mul.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''