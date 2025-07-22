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
        super(Model, self).__init__()
        self.conv_t2 = torch.nn.ConvTranspose2d(35, 48, 5, stride=1, padding=0, bias=True)
        self.conv_t3 = torch.nn.ConvTranspose2d(35, 48, 6, stride=3, padding=0, bias=True)

    def forward(self, x10):
        f1 = self.conv_t2(x10)
        f2 = f1 > 0
        f3 = f1 * -0.132
        f4 = torch.where(f2, f1, f3)
        f5 = f4 + self.conv_t3(x10)
        return torch.nn.functional.adaptive_avg_pool2d(f5, (1, 1))



func = Model().to('cpu')


x10 = torch.randn(5, 35, 26, 92)

test_inputs = [x10]

# JIT_FAIL
'''
direct:
The size of tensor a (96) must match the size of tensor b (279) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(5, 48, 30, 96)), FakeTensor(..., size=(5, 48, 81, 279))), **{}):
Attempting to broadcast a dimension of length 279 at -1! Mismatching argument at index 1 had torch.Size([5, 48, 81, 279]); but expected shape should be broadcastable to [5, 48, 30, 96]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''