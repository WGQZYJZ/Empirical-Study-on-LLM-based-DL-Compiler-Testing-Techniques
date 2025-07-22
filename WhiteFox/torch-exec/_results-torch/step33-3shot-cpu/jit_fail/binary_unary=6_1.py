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

class Net1(nn.Module):

    def __init__(self):
        super(Net1, self).__init__()
        self.l1 = nn.Linear(5, 2, 1)
        self.l2 = nn.Linear(5, 1, 1)

    def forward(self, x1, x2):
        x = torch.cat((x1, x2), 0)
        x = self.l1(x) - x1
        x0 = self.l2(x)
        return x0

class Net2(nn.Module):

    def __init__(self):
        super(Net2, self).__init__()
        self.l1 = nn.Linear(5, 2, 1)
        self.l2 = nn.Linear(5, 1, 1)

    def forward(self, x1, x2):
        x = torch.cat((x1, x2), 0)
        x = self.l1(x) - x2
        x0 = self.l2(x)
        return x0


func = Net2().to('cpu')


x1 = torch.randn(1, 5)

x2 = torch.randn(1, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (5) at non-singleton dimension 1

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(2, 2)), FakeTensor(..., size=(1, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([1, 5]); but expected shape should be broadcastable to [2, 2]

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''