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

    def forward(self, x1):
        v1 = x1.permute(0, 3, 2, 1)
        return v1.permute(0, (- 1), (- 2), (- 3))




func = Model().to('cuda')



x1 = torch.randn(1, 1, 2, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 5 is not equal to len(dims) = 4

jit:
Failed running call_method permute(*(FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2, 2)), 0, 3, 2, 1), **{}):
Attempting to permute a tensor of rank 5, but received a permutation of length 4!

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''