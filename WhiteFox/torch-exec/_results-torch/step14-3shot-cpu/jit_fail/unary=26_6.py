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
        self.c1 = torch.nn.Conv2d(3, 6, 5)
        self.c2 = torch.nn.ConvTranspose2d(6, 16, 3)
        self.p1 = torch.nn.MaxPool2d(2, stride=2)
        self.relu1 = torch.nn.ReLU()
        self.relu2 = torch.nn.ReLU()

    def forward(self, x):
        x = self.c1(x)
        x_clone = self.c2(x)
        x_pool = self.p1(x)
        x_out1 = self.relu1(x)
        x_out2 = self.relu2(x_clone)
        x_out3 = self.relu2(x_pool)
        return x_out1 * x_out2 * x_out3



func = Model().to('cpu')


x = torch.randn(1, 3, 20, 20)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (18) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 6, 16, 16)), FakeTensor(..., size=(1, 16, 18, 18))), **{}):
Attempting to broadcast a dimension of length 18 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 18, 18]); but expected shape should be broadcastable to [1, 6, 16, 16]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''