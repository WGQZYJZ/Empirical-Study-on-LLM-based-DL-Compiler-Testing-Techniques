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

    def forward(self, x, kernal, mask):
        qmk = (x @ kernal.transpose((- 2), (- 1)))
        output = torch.softmax(qmk, dim=(- 1))
        return output




func = Model().to('cuda')



Q = torch.randn(1, 64, 56, 56)



K = torch.randn(1, 16, 16, 64)



mask = (torch.rand(1, 16, 16) > 0.7).fill_((- 100000000.0))


test_inputs = [Q, K, mask]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 56, 56)), FakeTensor(..., device='cuda:0', size=(1, 16, 64, 16))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''