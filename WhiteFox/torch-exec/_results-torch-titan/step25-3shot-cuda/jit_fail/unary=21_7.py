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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 58, 14, stride=1)
        self.tanh = torch.nn.Tanh()

    def forward(self, x1):
        x2 = x1.permute(0, 2, 1)
        x3 = torch.tanh(x2)
        return x3




func = ModelTanh().to('cuda')



x = torch.randn(1, 1, 12, 16)


test_inputs = [x]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 4 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., device='cuda:0', size=(1, 1, 12, 16)), 0, 2, 1), **{}):
Attempting to permute a tensor of rank 4, but received a permutation of length 3!

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''