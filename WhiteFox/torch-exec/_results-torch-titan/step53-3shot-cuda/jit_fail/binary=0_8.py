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
        self.bn = torch.nn.BatchNorm2d(19)

    def forward(self, x1, x2, x3, other=None, padding1=None):
        v1 = self.bn(torch.cat([x1, x2, x3], dim=1))
        if (other == None):
            other = torch.randn(v1.shape)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 7, 13, 16)



x2 = torch.randn(1, 7, 13, 16)



x3 = torch.randn(1, 13, 8, 8)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 13 but got size 8 for tensor number 2 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x74d3d68699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 7, 13, 16)), FakeTensor(..., device='cuda:0', size=(1, 7, 13, 16)), FakeTensor(..., device='cuda:0', size=(1, 13, 8, 8))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 13 but got 8 for tensor number 2 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''