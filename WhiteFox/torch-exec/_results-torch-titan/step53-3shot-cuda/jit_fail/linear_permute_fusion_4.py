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
        self.linear = torch.nn.Linear(2, 2, bias=False)

    def forward(self, x3):
        v0 = x3
        v1 = v0.size()
        v2 = v0.view(v1[0], (- 1))
        v3 = v2.permute(0, 2, 1)
        v4 = v3.contiguous()
        v5 = self.linear(v4)
        return v5




func = Model().to('cuda')



x3 = torch.randn(1, 2, 2)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 2 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., device='cuda:0', size=(1, 4)), 0, 2, 1), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''