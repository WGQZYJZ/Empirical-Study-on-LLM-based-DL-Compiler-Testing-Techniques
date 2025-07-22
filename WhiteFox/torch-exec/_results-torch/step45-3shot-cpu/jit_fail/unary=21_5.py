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

class MyModule(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 43, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(1, 86, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        y1 = self.conv1(x1)
        y2 = self.conv2(x2)
        y3 = torch.tanh(y1 + y2)
        return y3



func = MyModule().to('cpu')


x1 = torch.randn(1, 1, 20, 20)

x2 = torch.randn(1, 1, 20, 20)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (43) must match the size of tensor b (86) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 43, 22, 22)), FakeTensor(..., size=(1, 86, 22, 22))), **{}):
The size of tensor a (43) must match the size of tensor b (86) at non-singleton dimension 1)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''