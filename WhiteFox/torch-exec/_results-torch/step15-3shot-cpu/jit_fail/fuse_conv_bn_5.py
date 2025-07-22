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

class M1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        y1 = self.conv(x1)
        y2 = self.bn(x1)
        return torch.add(y2, y1)



func = M1().to('cpu')


x1 = torch.randn(1, 3, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 3

jit:
Failed running call_function <built-in method add of type object at 0x75431a596ec0>(*(FakeTensor(..., size=(1, 3, 4, 4)), FakeTensor(..., size=(1, 3, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 2, 2]); but expected shape should be broadcastable to [1, 3, 4, 4]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''