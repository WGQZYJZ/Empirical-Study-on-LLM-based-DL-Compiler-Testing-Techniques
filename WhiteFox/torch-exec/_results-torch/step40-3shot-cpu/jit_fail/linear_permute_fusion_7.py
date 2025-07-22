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
        self.linear = torch.nn.Linear(2, 2).cuda()
        self.linear1 = torch.nn.Linear(2, 2).cuda()

    def forward(self, x1):
        v4 = x1.cuda()
        v5 = torch.nn.functional.relu(v4)
        v1 = torch.nn.functional.linear(v4, self.linear.weight, self.linear.bias)
        v2 = torch.nn.functional.relu6(v1)
        v3 = v2.permute(0, 1, 3, 2)
        v6 = torch.min(v3, dim=2, keepdim=False, out=None).values
        v7 = torch.nn.functional.linear(v5.permute(0, 2, 1), self.linear1.weight, self.linear1.bias)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2, device='cuda')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, s0, 2)), Parameter(FakeTensor(..., size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''