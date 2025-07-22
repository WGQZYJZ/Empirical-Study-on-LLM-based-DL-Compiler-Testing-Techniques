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
        self.conv0 = torch.nn.Conv2d(3, 11, 1, stride=1, padding=0)
        self.conv1 = torch.nn.Conv2d(3, 11, 1, stride=1, padding=1)

    def forward(self, input, padding0=None, padding1=None):
        x1 = self.conv0(input)
        if (padding0 == None):
            padding0 = torch.randn(x1.shape)
        x2 = self.conv1(input)
        if (padding1 == None):
            padding1 = torch.randn(x2.shape)
        x3 = (x1 + x2)
        return x3




func = Model().to('cuda')



input = torch.randn(1, 3, 64, 64)


test_inputs = [input]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (66) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 11, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 11, 66, 66))), **{}):
Attempting to broadcast a dimension of length 66 at -1! Mismatching argument at index 1 had torch.Size([1, 11, 66, 66]); but expected shape should be broadcastable to [1, 11, 64, 64]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''