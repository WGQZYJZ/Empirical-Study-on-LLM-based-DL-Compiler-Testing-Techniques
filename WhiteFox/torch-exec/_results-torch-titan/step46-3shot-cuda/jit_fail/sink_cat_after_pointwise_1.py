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
        t = torch.ones(10, 20)
        y = torch.cat((t, x), dim=0)
        return y.view(y.shape[0], (- 1)).relu()




func = Model().to('cuda')



x = torch.ones(1, 20)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument tensors in method wrapper_CUDA_cat)

jit:
Failed running call_function <built-in method cat of type object at 0x7c9ed40699e0>(*((FakeTensor(..., size=(10, 20)), FakeTensor(..., device='cuda:0', size=(1, 20))),), **{'dim': 0}):
Unhandled FakeTensor Device Propagation for aten.cat.default, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''