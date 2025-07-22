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
        self.conv1 = torch.nn.Conv2d(3, 25, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(25, 96, 4, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(96)

    def forward(self, x1):
        s1 = self.conv1(x1)
        s2 = self.conv2(s1)
        s3 = (s2 + 3)
        s4 = torch.clamp_min(s3, 0)
        s5 = torch.clamp_max(s4, 6)
        s6 = (s1 * s5)
        s7 = (s6 / 6)
        s8 = self.bn(s7)
        return s7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (256) must match the size of tensor b (255) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 25, 256, 256)), FakeTensor(..., device='cuda:0', size=(1, 96, 255, 255))), **{}):
Attempting to broadcast a dimension of length 255 at -1! Mismatching argument at index 1 had torch.Size([1, 96, 255, 255]); but expected shape should be broadcastable to [1, 25, 256, 256]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''