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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 64, (2, 2), stride=(2, 2))

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tensor([123.0, 456.0, 789.0])
        v3 = v1 * v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(2, 3, 3, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (3) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(2, 64, 6, 6)), FakeTensor(..., size=(3,))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([3]); but expected shape should be broadcastable to [2, 64, 6, 6]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''