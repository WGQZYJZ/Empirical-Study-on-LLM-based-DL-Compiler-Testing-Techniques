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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v4 = x1.to('cpu')
        v1 = 5
        v2 = (v1 + 6)
        v4 = v4.to('cpu')
        v2 = torch.nn.functional.linear(v4, self.linear.weight, self.linear.bias)
        v5 = v2.permute(0, 2, 1)
        v4 = v4.to('cpu')
        v5 = v2.permute(0, 2, 1)
        v6 = v5.to('cpu')
        v7 = torch.nn.functional.linear(v6, self.linear.weight, self.linear.bias)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, device='cuda')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(2,), requires_grad=True))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''