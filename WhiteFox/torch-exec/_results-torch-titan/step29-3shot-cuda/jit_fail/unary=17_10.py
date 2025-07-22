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
        self.up = torch.nn.ConvTranspose2d(512, 256, 2, stride=2)
        self.conv = torch.nn.ConvTranspose2d(512, 128, 1, stride=1, padding=0)
        self.conv1 = torch.nn.ConvTranspose2d(256, 64, 1, stride=1, padding=0)
        self.fc = torch.nn.ConvTranspose2d(64, 32, 1, stride=1, padding=0)
        self.conv2 = torch.nn.ConvTranspose2d(32, 1, 1, stride=1, padding=0)

    def forward(self, x1):
        v11 = self.up(x1)
        v11 = F.relu(v11)
        v12 = self.conv(x1)
        v12 = F.relu(v12)
        v13 = torch.add(v11, v12)
        v13 = self.conv1(v13)
        v13 = F.relu(v13)
        v15 = self.fc(v13)
        v15 = F.relu(v15)
        v16 = self.conv2(v15)
        v16 = torch.sigmoid(v16)
        return v16




func = Model().to('cuda')



x1 = torch.randn(1, 512, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 3

jit:
Failed running call_function <built-in method add of type object at 0x7658ab2699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 256, 4, 4)), FakeTensor(..., device='cuda:0', size=(1, 128, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([1, 128, 2, 2]); but expected shape should be broadcastable to [1, 256, 4, 4]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''