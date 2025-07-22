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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.addmm = torch.addmm
        self.cat = torch.cat

    def forward(self, x):
        x = self.addmm(x, torch.rand(2, 2), torch.rand(2, 2))
        x = self.cat([x, x], dim=1)
        y = (x + x)
        return y




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_function <built-in method addmm of type object at 0x7390d00699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2)), FakeTensor(..., size=(2, 2)), FakeTensor(..., size=(2, 2))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''