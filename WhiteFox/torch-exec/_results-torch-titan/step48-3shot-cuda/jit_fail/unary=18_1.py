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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=5, kernel_size=[3, 3], stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(in_channels=5, out_channels=8, kernel_size=[1, 1], stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(in_channels=8, out_channels=7, kernel_size=[1, 1], stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v2 = torch.mul(v2, self.conv3(v2))
        v3 = torch.sigmoid(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (7) at non-singleton dimension 1

jit:
Failed running call_function <built-in method mul of type object at 0x7d128be699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 62, 62)), FakeTensor(..., device='cuda:0', size=(1, 7, 62, 62))), **{}):
Attempting to broadcast a dimension of length 7 at -3! Mismatching argument at index 1 had torch.Size([1, 7, 62, 62]); but expected shape should be broadcastable to [1, 8, 62, 62]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''