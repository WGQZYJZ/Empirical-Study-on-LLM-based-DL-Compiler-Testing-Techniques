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
        self.conv1 = torch.nn.Conv2d(3, 6, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(6, 6, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.max(v1, v2)
        v4 = torch.max(v2, v3)
        v5 = torch.relu(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (258) must match the size of tensor b (260) at non-singleton dimension 3

jit:
Failed running call_function <built-in method max of type object at 0x785bda4699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 6, 258, 258)), FakeTensor(..., device='cuda:0', size=(1, 6, 260, 260))), **{}):
Attempting to broadcast a dimension of length 260 at -1! Mismatching argument at index 1 had torch.Size([1, 6, 260, 260]); but expected shape should be broadcastable to [1, 6, 258, 258]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''