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

    def __init__(self, kernel_size, padding):
        super().__init__()
        self.conv_t1 = torch.nn.ConvTranspose2d(768, 624, kernel_size, stride=1, dilation=3, padding=padding)
        self.conv_t2 = torch.nn.ConvTranspose2d(624, 768, 1, stride=1)

    def forward(self, x1):
        x2 = self.conv_t1(x1)
        x3 = self.conv_t2(x2)
        x4 = x3 < 0
        x5 = x2 < 0
        x6 = x5 | x4
        x7 = x2.view(2304)
        return (x6, x7 + x2 / 3.0)


kernel_size = 3
padding = 1

func = Model(kernel_size, padding).to('cpu')


x1 = torch.randn(16, 768, 108, 108)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (624) must match the size of tensor b (768) at non-singleton dimension 1

jit:
Failed running call_function <built-in function or_>(*(FakeTensor(..., size=(16, 624, 112, 112), dtype=torch.bool), FakeTensor(..., size=(16, 768, 112, 112), dtype=torch.bool)), **{}):
Attempting to broadcast a dimension of length 768 at -3! Mismatching argument at index 1 had torch.Size([16, 768, 112, 112]); but expected shape should be broadcastable to [16, 624, 112, 112]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''