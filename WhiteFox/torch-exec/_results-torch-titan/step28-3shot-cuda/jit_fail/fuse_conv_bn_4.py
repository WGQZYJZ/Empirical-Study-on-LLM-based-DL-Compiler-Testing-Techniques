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
        self.conv1 = torch.nn.Conv2d(5, 5, 2)
        self.bn1 = torch.nn.BatchNorm2d(5)
        self.bn2 = torch.nn.BatchNorm2d(5)
        self.conv2 = torch.nn.Conv2d(3, 5, 1)

    def forward(self, x2):
        x1 = self.conv1(x2)
        x3 = self.bn1(x1)
        x4 = self.bn2(x2)
        x5 = self.conv2(((x1 + x3) + x4))
        return x5




func = Model().to('cuda')



x2 = torch.randn(1, 5, 4, 4)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 3, 3)), FakeTensor(..., device='cuda:0', size=(1, 5, 4, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 5, 4, 4]); but expected shape should be broadcastable to [1, 5, 3, 3]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''