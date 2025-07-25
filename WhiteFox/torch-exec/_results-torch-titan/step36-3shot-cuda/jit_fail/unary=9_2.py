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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_conv = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = (x2 - v1)
        v3 = v2.clamp(0, 6)
        v4 = v3.div(6)
        v5 = self.other_conv(v4)
        v6 = (x2 - v5)
        v7 = v6.clamp(0, 6)
        v8 = v7.div(6)
        return v8




func = Model().to('cuda')



x1 = torch.randn(5, 3, 64, 64)



x2 = torch.randn(1, 8, 32, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (66) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)), FakeTensor(..., device='cuda:0', size=(5, 8, 66, 66))), **{}):
Attempting to broadcast a dimension of length 66 at -1! Mismatching argument at index 1 had torch.Size([5, 8, 66, 66]); but expected shape should be broadcastable to [1, 8, 32, 32]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''