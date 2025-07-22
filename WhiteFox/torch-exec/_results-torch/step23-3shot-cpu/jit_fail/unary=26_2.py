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
        self.conv_t0 = torch.nn.ConvTranspose1d(1, 1, 3, stride=1)
        self.conv_t1 = torch.nn.ConvTranspose1d(1, 1, 3, stride=1)

    def forward(self, input_tensor):
        y = self.conv_t0(input_tensor)
        _mask = y > 0
        _tensor = torch.where(_mask, y, 0.7 * y)
        return self.conv_t1(_tensor) + _tensor



func = Model().to('cpu')


input_tensor = torch.randn(1, 1, 3)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
The size of tensor a (7) must match the size of tensor b (5) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 1, 7)), FakeTensor(..., size=(1, 1, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 5]); but expected shape should be broadcastable to [1, 1, 7]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''