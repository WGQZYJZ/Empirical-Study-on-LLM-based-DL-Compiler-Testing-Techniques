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
        self.conv1 = torch.nn.Conv2d(512, 64, kernel_size=(7, 7), stride=(1, 1), padding=(2, 2), bias=False)
        self.conv2 = torch.nn.ConvTranspose2d(64, 96, kernel_size=(2, 2), stride=(2, 2))
        self.conv3 = torch.nn.ConvTranspose2d(96, 128, kernel_size=(2, 2), stride=(1, 1), padding=(1, 1))
        self.conv4 = torch.nn.ConvTranspose2d(128, 32, kernel_size=(3, 3), stride=(1, 1), padding=(3, 3))

    def forward(self, x1):
        out = torch.nn.functional.relu(self.conv1(x1))
        out = torch.add(-torch.nn.functional.relu(self.conv2(out)), out)
        out = torch.add(-torch.nn.functional.relu(self.conv3(out)), out)
        out = torch.add(-torch.nn.functional.relu(self.conv4(out)), out)
        return out



func = Model().to('cpu')


x1 = torch.randn(1, 512, 7, 7)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (5) at non-singleton dimension 3

jit:
Failed running call_function <built-in method add of type object at 0x79e570996ec0>(*(FakeTensor(..., size=(1, 96, 10, 10)), FakeTensor(..., size=(1, 64, 5, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([1, 64, 5, 5]); but expected shape should be broadcastable to [1, 96, 10, 10]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''