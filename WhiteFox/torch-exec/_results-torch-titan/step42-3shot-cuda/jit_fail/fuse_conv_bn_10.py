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
        self.conv1 = torch.nn.Conv2d(1, 1, 3, groups=1, bias=True)
        self.bn1 = torch.nn.BatchNorm2d(1, affine=True, track_running_stats=True)
        self.conv2 = torch.nn.Conv2d(1, 1, 3, groups=1, bias=True)
        self.bn2 = torch.nn.BatchNorm2d(1, affine=True, track_running_stats=True)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        y = self.conv2(x)
        y = self.bn2(y)
        z = (x * y)
        return z




func = Model().to('cuda')



x = torch.randn(1, 1, 6, 6)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 4, 4)), FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 2, 2]); but expected shape should be broadcastable to [1, 1, 4, 4]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''