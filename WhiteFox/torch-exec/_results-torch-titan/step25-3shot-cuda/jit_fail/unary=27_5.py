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

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 6, 6, stride=1, padding=1)
        self.t1 = torch.nn.ReLU()
        self.min = min
        self.max = max

    def forward(self, input, min, max):
        v0 = torch.zeros_like(input.mul(0))
        t1 = v0
        conv_input = (t1.mul(0) + input)
        v11 = self.conv(conv_input)
        relu_input = torch.clamp_max(v11, 0)
        v12 = self.t1(relu_input)
        v2 = torch.clamp_max(v12, max)
        v3 = (v2.mul(0) + input)
        return v3




min = 2


max = 1


func = Model(min, max).to('cuda')



input = torch.randn(1, 3, 52, 52)

min = 1
max = 1

test_inputs = [input, min, max]

# JIT_FAIL
'''
direct:
The size of tensor a (49) must match the size of tensor b (52) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 6, 49, 49)), FakeTensor(..., device='cuda:0', size=(1, 3, 52, 52))), **{}):
Attempting to broadcast a dimension of length 52 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 52, 52]); but expected shape should be broadcastable to [1, 6, 49, 49]

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''