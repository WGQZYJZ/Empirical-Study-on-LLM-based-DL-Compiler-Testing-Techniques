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
        self.conv1 = torch.nn.Conv2d(128, 64, 1, stride=1, padding=0, bias=False)
        self.conv2 = torch.nn.Conv2d(128, 64, (1, 7), stride=1, padding=(0, 5), bias=False)

    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = self.conv2(x1)
        t3 = t1 + t2
        t4 = t3.clamp(0, 6)
        t5 = t1 - t2
        t6 = t5.clamp(0, 6)
        t7 = t4 * t6
        t8 = t7 / 6
        return t8



func = Model().to('cpu')


x1 = torch.randn(1, 128, 64, 192)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (192) must match the size of tensor b (196) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 64, 64, 192)), FakeTensor(..., size=(1, 64, 64, 196))), **{}):
Attempting to broadcast a dimension of length 196 at -1! Mismatching argument at index 1 had torch.Size([1, 64, 64, 196]); but expected shape should be broadcastable to [1, 64, 64, 192]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''