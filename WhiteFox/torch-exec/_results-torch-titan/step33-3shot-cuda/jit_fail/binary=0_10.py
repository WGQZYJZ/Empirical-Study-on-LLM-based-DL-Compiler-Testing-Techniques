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
        self.conva = torch.nn.Conv2d(32, 96, 1, stride=1, padding=0)
        self.convb = torch.nn.Conv2d(96, 128, 1, stride=1, padding=0)

    def forward(self, x1, x2=torch.randn(1, 1, 0, 0), x3=None):
        v1 = self.conva(x1)
        v2 = (v1 + 3)
        if (not x3):
            x3 = (v2 + x2).view((list(v2.shape) + [(- 1)])).contiguous()
        v3 = self.convb(x3)
        v4 = (v3 + 2)
        return v4




func = Model().to('cuda')



x1 = torch.randn(2, 32, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (0) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(2, 96, 4, 4)), FakeTensor(..., size=(1, 1, 0, 0))), **{}):
Attempting to broadcast a dimension of length 0 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 0, 0]); but expected shape should be broadcastable to [2, 96, 4, 4]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''