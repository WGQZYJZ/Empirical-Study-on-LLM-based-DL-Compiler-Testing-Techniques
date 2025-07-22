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
        self.conv = torch.nn.Conv2d(4, 8, 1, stride=1, padding=4)

    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if (other is None):
            v1 = (v1 + x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 4, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (72) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 72, 72)), FakeTensor(..., device='cuda:0', size=(1, 4, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 4, 64, 64]); but expected shape should be broadcastable to [1, 8, 72, 72]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''