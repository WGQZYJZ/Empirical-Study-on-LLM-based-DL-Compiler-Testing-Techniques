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
        self.linear = torch.nn.Linear(2, 2)
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x4):
        t1 = torch.nn.functional.linear(x4, self.linear.weight, self.linear.bias)
        t2 = torch.nn.functional.linear(t1, self.linear1.weight, self.linear1.bias)
        v3 = torch.nn.functional.linear(t2, self.linear1.weight, self.linear1.bias)
        v2 = torch.nn.functional.linear(v3, self.linear2.weight, self.linear2.bias)
        v1 = v2.permute(0, 2, 1)
        return v1




func = Model().to('cuda')



x4 = torch.randn(2, 2, 2, 2)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 4 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., device='cuda:0', size=(2, 2, 2, 2)), 0, 2, 1), **{}):
Attempting to permute a tensor of rank 4, but received a permutation of length 3!

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''