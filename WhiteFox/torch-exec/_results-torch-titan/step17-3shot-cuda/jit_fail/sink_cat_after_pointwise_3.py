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
        y = (torch.relu(x) + torch.tanh(x))
        y = y.permute(1, 0, 2, 3).unsqueeze(1)
        y = torch.permute(y, (3,))
        y = y.permute(1, 0)
        y = y.permute(1, 0, 2).reshape(2, (- 1))
        return y




func = Model().to('cuda')



x = torch.randn(2, 3, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 5 is not equal to len(dims) = 1

jit:
Failed running call_function <built-in method permute of type object at 0x79eed08699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 1, 2, 4, 4)), (3,)), **{}):
Attempting to permute a tensor of rank 5, but received a permutation of length 1!

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''