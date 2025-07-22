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

    def forward(self, x):
        x = x.permute(0, 2, 3, 1).view(12, (- 1))
        y = x.tanh()
        z = y.view(x.shape[0], x.shape[1], x.shape[2], x.shape[4])
        x = x.view((z.shape[0] + x.shape[0]), z.shape[1], z.shape[2], z.shape[3])
        x = torch.cat([x, z], dim=0)
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 3 is not equal to len(dims) = 4

jit:
Failed running call_method permute(*(FakeTensor(..., device='cuda:0', size=(2, 3, 4)), 0, 2, 3, 1), **{}):
Dimension out of range (expected to be in range of [-3, 2], but got 3)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''