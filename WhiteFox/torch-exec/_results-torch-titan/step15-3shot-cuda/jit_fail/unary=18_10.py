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



class model(nn.Module):

    def __init__(self, input_channels, output_channels, kernel_size):
        super(model, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=1)
        self.conv2 = nn.Conv2d(16, 8, kernel_size=1)
        self.conv3 = nn.Conv2d(8, 8, kernel_size=1)
        self.conv4 = nn.Conv2d(4, 10, kernel_size=3, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv3(v4)
        v6 = torch.sigmoid(v5)
        v7 = (v2 + v6)
        v8 = self.conv4(v7)
        v9 = torch.sigmoid(v8)
        return v9



input_channels = 1
output_channels = 1
kernel_size = 1

func = model(input_channels, output_channels, kernel_size).to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64))), **{}):
Attempting to broadcast a dimension of length 8 at -3! Mismatching argument at index 1 had torch.Size([1, 8, 64, 64]); but expected shape should be broadcastable to [1, 16, 64, 64]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''