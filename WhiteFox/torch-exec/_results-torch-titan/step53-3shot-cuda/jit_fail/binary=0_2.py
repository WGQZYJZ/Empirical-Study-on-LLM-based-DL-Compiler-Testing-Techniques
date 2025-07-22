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
        self.conv = torch.nn.Conv2d(9, 15, 1, stride=8, padding=0)

    def forward(self, x1, other=None, padding1=None):
        v1 = self.conv(x1)
        if (other == None):
            other = torch.randn(padding1.shape)
        if (padding1 == None):
            padding1 = torch.randn(other.shape)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 9, 15, 15)



other = torch.randn(1, 4, 15, 15)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (15) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 15, 2, 2)), FakeTensor(..., device='cuda:0', size=(1, 4, 15, 15))), **{}):
Attempting to broadcast a dimension of length 15 at -1! Mismatching argument at index 1 had torch.Size([1, 4, 15, 15]); but expected shape should be broadcastable to [1, 15, 2, 2]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''