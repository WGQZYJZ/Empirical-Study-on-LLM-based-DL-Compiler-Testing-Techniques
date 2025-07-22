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

    def __init__(self, negative_slope):
        super().__init__()
        self.weight = torch.nn.Parameter(torch.Tensor([0.5]))

    def forward(self, x1):
        v1 = torch.matmul(x1, self.weight.T)
        v2 = v1 > 0
        v3 = v1 * self.weight[0]
        v4 = torch.where(v2, v1, v3)
        return v4


negative_slope = 1
func = Model(0.1).to('cuda')


x1 = torch.randn(2, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
size mismatch, got input (2), mat (2x8), vec (1)

jit:
Failed running call_function <built-in method matmul of type object at 0x709b4a396ec0>(*(FakeTensor(..., device='cuda:0', size=(2, 8)), FakeTensor(..., device='cuda:0', size=(1,), requires_grad=True)), **{}):
size mismatch, got input (2x8), vec (1)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''