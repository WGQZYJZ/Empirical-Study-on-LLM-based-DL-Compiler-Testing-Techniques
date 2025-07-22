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
        self.conv = torch.nn.Conv2d(1, 12, 5, stride=1, padding=0, dilation=1)
        self.conv1 = torch.nn.Conv2d(12, 4, 3, stride=1, padding=0, dilation=1)

    def forward(self, x2):
        v1 = self.conv(x2)
        v2 = self.conv1(v1)
        v3 = (v2 + 1)
        v4 = (v1 * v3)
        return v4




func = Model().to('cuda')



x2 = torch.randn(1, 1, 80, 80)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
The size of tensor a (76) must match the size of tensor b (74) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 12, 76, 76)), FakeTensor(..., device='cuda:0', size=(1, 4, 74, 74))), **{}):
Attempting to broadcast a dimension of length 74 at -1! Mismatching argument at index 1 had torch.Size([1, 4, 74, 74]); but expected shape should be broadcastable to [1, 12, 76, 76]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''