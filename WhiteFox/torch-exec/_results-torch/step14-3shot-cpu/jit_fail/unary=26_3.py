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
        self.conv_t = torch.nn.ConvTranspose2d(192, 128, (1, 1), stride=(1, 1))
        self.batch_norm = torch.nn.BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.relu = torch.nn.ReLU()

    def forward(self, x0):
        identity = x0
        v0 = self.conv_t(x0)
        v1 = self.batch_norm(v0)
        v2 = self.relu(v1)
        v3 = torch.add(identity, v2)
        return v3



func = Model().to('cpu')


x0 = torch.randn(1, 192, 7, 7)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
The size of tensor a (192) must match the size of tensor b (128) at non-singleton dimension 1

jit:
Failed running call_function <built-in method add of type object at 0x7c889d196ec0>(*(FakeTensor(..., size=(1, 192, 7, 7)), FakeTensor(..., size=(1, 128, 7, 7))), **{}):
Attempting to broadcast a dimension of length 128 at -3! Mismatching argument at index 1 had torch.Size([1, 128, 7, 7]); but expected shape should be broadcastable to [1, 192, 7, 7]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''