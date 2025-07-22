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
        self.convTranspose_15 = torch.nn.ConvTranspose2d(20, 60, 3, stride=2, padding=1)
        self.convTranspose_25 = torch.nn.ConvTranspose2d(60, 68, 3, stride=2, padding=1)
        self.convTranspose_35 = torch.nn.ConvTranspose2d(68, 60, 3, stride=2, padding=1)
        self.convTranspose_45 = torch.nn.ConvTranspose2d(60, 7, 3, stride=2, padding=1)

    def forward(self, x):
        output = self.convTranspose_15(x)
        output = output + x
        output = self.convTranspose_25(output)
        output = self.convTranspose_35(output)
        output = output + x
        output = self.convTranspose_45(output)
        return output



func = Model().to('cpu')


x = torch.randn(1, 20, 30, 20)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (39) must match the size of tensor b (20) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 60, 59, 39)), FakeTensor(..., size=(1, 20, 30, 20))), **{}):
Attempting to broadcast a dimension of length 20 at -1! Mismatching argument at index 1 had torch.Size([1, 20, 30, 20]); but expected shape should be broadcastable to [1, 60, 59, 39]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''