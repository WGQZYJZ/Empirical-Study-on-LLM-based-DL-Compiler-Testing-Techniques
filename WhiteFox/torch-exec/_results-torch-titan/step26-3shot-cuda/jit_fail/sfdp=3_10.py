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
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = self.linear(x1)
        k = torch.tensor([[0.028343, 0.010301], [0.19309, 0.049428], [0.0010161, 0.0036473]])
        scale = torch.tensor(10.0)
        v2 = (torch.matmul(v1, k) * scale)
        v3 = torch.nn.functional.softmax(v2, dim=0)
        v4 = torch.nn.functional.dropout(v3, p=0.5)
        v5 = torch.matmul(v4, k.transpose(0, 1))
        output = (v5 * scale)
        return output



func = Model().to('cuda')



x1 = torch.randn(3, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method matmul of type object at 0x77e0c92699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., size=(3, 2))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''