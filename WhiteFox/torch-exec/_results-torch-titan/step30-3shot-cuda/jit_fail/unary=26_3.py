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
        self.conv_t1 = torch.nn.ConvTranspose3d(1, 1, 2, stride=2)
        self.conv_t2 = torch.nn.ConvTranspose3d(1, 1, 2, stride=2)
        self.negative_slope = negative_slope

    def forward(self, x):
        t1 = self.conv_t1(x)
        t2 = torch.le(t1, 0.9)
        t3 = (t1 * self.negative_slope)
        t4 = torch.where(t2, t1, t3)
        t5 = self.conv_t2(t4)
        t6 = torch.le(t5, 0.708)
        t7 = (t5 * self.negative_slope)
        t8 = torch.where(t6, t4, t7)
        return t8




negative_slope = 0.13


func = Model(negative_slope).to('cuda')



x = torch.randn(4, 1, 2, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (4) at non-singleton dimension 4

jit:
Failed running call_function <built-in method where of type object at 0x7c0bddc699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 1, 8, 8, 8), dtype=torch.bool), FakeTensor(..., device='cuda:0', size=(4, 1, 4, 4, 4)), FakeTensor(..., device='cuda:0', size=(4, 1, 8, 8, 8))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([4, 1, 4, 4, 4]); but expected shape should be broadcastable to [4, 1, 8, 8, 8]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''