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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 1)
        self.conv4 = torch.nn.Conv2d(3, 8, 1)
        self.conv5 = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = self.conv3(x1)
        v4 = self.conv4(x2)
        v5 = ((((v1 + v2) + v3) + v4) + v2)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)



x2 = torch.randn(1, 3, 32, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (34) must match the size of tensor b (32) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 34, 34)), FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 32, 32]); but expected shape should be broadcastable to [1, 8, 34, 34]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''