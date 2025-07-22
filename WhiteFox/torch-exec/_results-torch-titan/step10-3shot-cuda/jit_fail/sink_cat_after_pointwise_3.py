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
        x = x.clone()
        x = x.repeat(2, 1, 1)
        y = x.reshape(x).shape[2]
        z = x.view(2, (x.shape[0] * x.shape[1]), (x.shape[2] * x.shape[3]))
        return z




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
reshape(): argument 'shape' (position 1) must be tuple of ints, but found element of type Tensor at pos 0

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(4, 3, 4)), FakeTensor(..., device='cuda:0', size=(4, 3, 4))), **{}):
reshape(): argument 'shape' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''