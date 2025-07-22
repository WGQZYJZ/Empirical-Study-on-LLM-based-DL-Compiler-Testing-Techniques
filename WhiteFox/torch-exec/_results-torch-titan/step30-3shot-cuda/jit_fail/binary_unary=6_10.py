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

    def forward(self, x1, weight=torch.randn((45, 10)), bias=torch.randn((10,))):
        v1 = torch.matmul(x1, weight)
        return (v1 - bias)



func = Model().to('cuda')



x1 = torch.randn(128, 45)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method matmul of type object at 0x77ed53e699e0>(*(FakeTensor(..., device='cuda:0', size=(128, 45)), FakeTensor(..., size=(45, 10))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''