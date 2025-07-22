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
        self.conv1 = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 4, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 4, 5, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 4, 7, stride=1, padding=1)

    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = self.conv2(x1)
        t3 = self.conv3(x1)
        t4 = self.conv4(x1)
        t5 = t1 + t2 + t3 + t4
        t6 = t5 / 4
        return t6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (130) must match the size of tensor b (128) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 4, 130, 130)), FakeTensor(..., size=(1, 4, 128, 128))), **{}):
Attempting to broadcast a dimension of length 128 at -1! Mismatching argument at index 1 had torch.Size([1, 4, 128, 128]); but expected shape should be broadcastable to [1, 4, 130, 130]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''