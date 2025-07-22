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
        self.conv_t = torch.nn.ConvTranspose2d(1, out_channels=1, kernel_size=3, bias=False)

    def forward(self, x0):
        v0 = torch.permute(x0, [0, 2, 1])
        v0 = torch.permute(v0, [0, 2, 1])
        v1 = self.conv_t(v0)
        v2 = torch.sigmoid(v1)
        v3 = torch.inverse(v2)
        v4 = torch.view(v3, [1, 128])
        return v4



func = Model().to('cpu')


x0 = torch.randn(1, 1, 64, 64)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 4 is not equal to len(dims) = 3

jit:
Failed running call_function <built-in method permute of type object at 0x726e8e996ec0>(*(FakeTensor(..., size=(1, 1, 64, 64)), [0, 2, 1]), **{}):
Attempting to permute a tensor of rank 4, but received a permutation of length 3!

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''