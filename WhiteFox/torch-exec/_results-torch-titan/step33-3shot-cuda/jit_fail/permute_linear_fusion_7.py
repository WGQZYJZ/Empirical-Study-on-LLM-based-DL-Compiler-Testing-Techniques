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
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(1, 1), stride=(1, 1), padding=(0,), dilation=(1,))
        self.gelu = torch.nn.GELU()

    def forward(self, x1):
        e1 = x1.permute(0, 2, 1)
        e2 = e1.permute(0, 2, 1)
        e2 = e2.permute(0, 2, 3)
        y = self.conv(e2)
        u = (((0.712 + (y * 0.241)) + 0.353) + y)
        x = u.flatten(1)
        y = self.gelu(x)
        return y




func = Model().to('cuda')



x1 = torch.randn(1, 1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 4 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2)), 0, 2, 1), **{}):
Attempting to permute a tensor of rank 4, but received a permutation of length 3!

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''