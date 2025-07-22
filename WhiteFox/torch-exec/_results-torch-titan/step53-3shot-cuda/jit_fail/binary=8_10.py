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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.conv3 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.bn3 = torch.nn.BatchNorm2d(16)
        self.bn4 = torch.nn.BatchNorm2d(16)
        self.conv5 = torch.nn.Conv2d(3, 32, 1, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(3, 32, 1, stride=1, padding=1)
        self.bn5 = torch.nn.BatchNorm2d(32)
        self.bn6 = torch.nn.BatchNorm2d(32)

    def forward(self, x1, x2):
        v1 = self.bn1(self.conv1(x1))
        v2 = self.bn2(self.conv2(x2))
        v3 = (v1 + v2)
        v4 = (v3 + self.bn3(self.conv3(x1)))
        v5 = (v4 * self.bn4(self.conv4(x2)))
        v6 = (v5 + self.bn5(self.conv5(x1)))
        v7 = (v6 + self.bn6(self.conv6(x2)))
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), FakeTensor(..., device='cuda:0', size=(1, 16, 66, 66))), **{}):
Attempting to broadcast a dimension of length 16 at -3! Mismatching argument at index 1 had torch.Size([1, 16, 66, 66]); but expected shape should be broadcastable to [1, 8, 66, 66]

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''