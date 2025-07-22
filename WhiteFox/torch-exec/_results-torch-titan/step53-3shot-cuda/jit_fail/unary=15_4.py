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
        self.conv1 = torch.nn.Conv2d(26, 48, 5, stride=1, padding=0, dilation=2)
        self.conv2 = torch.nn.Conv2d(48, 26, 3, stride=1, padding=1, dilation=1)
        self.conv3 = torch.nn.Conv2d(26, 26, 3, stride=1, padding=1, dilation=2)
        self.conv4 = torch.nn.Conv2d(26, 26, 1, stride=1, padding=0, dilation=1)
        self.conv5 = torch.nn.Conv2d(26, 14, 3, stride=1, padding=1, dilation=2)
        self.conv6 = torch.nn.Conv2d(14, 6, 3, stride=1, padding=1, dilation=2)
        self.conv7 = torch.nn.Conv2d(6, 6, 1, stride=1, padding=0, dilation=1)

    def forward(self, x1):
        v0 = torch.reshape(x1, [1, 26, 64, 64])
        v1 = self.conv1(v0)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = self.conv6(v5)
        v7 = self.conv7(v6)
        v8 = torch.reshape(v7, [(- 1), 6])
        v9 = torch.relu(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(64, 1, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 26, 64, 64]' is invalid for input of size 50176

jit:
Failed running call_function <built-in method reshape of type object at 0x76de4a4699e0>(*(FakeTensor(..., device='cuda:0', size=(64, 1, 28, 28)), [1, 26, 64, 64]), **{}):
shape '[1, 26, 64, 64]' is invalid for input of size 50176

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''