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

    def forward(self, x1):
        v1 = x1.flatten(start_dim=1)
        v2 = torch.tensor([2.67550209e-05, 8.7932609e-05, 4.33683297e-05, 2.56617851e-05, 1.62987153e-05, 1.14969637e-05, 8.48186018e-06, 6.5123352e-06], requires_grad=True)
        v3 = (torch.matmul(v1, v2) + 3)
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = (v5 / 6)
        return v6



func = Model().to('cuda')



x1 = torch.randn(1, 16, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat in method wrapper_CUDA_addmv_)

jit:
Failed running call_function <built-in method matmul of type object at 0x7094792699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 16)), FakeTensor(..., size=(8,), requires_grad=True)), **{}):
size mismatch, got input (1x16), vec (8)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''