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
        self.conv = torch.nn.Conv2d(48, 2, 3, stride=1, padding=2)

    def forward(self, x1, other):
        v1 = self.conv(x1)
        if (other is None):
            other = torch.randn(v1.shape)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 48, 32, 32)



other = torch.randn(1, 64, 32, 32)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
The size of tensor a (34) must match the size of tensor b (32) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 34, 34)), FakeTensor(..., device='cuda:0', size=(1, 64, 32, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([1, 64, 32, 32]); but expected shape should be broadcastable to [1, 2, 34, 34]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''