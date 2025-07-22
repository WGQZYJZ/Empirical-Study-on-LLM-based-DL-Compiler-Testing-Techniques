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
        x = torch.randn(3, x.shape[0], x.shape[1], x.shape[2], x.shape[2], dtype=torch.double)
        x.to(dtype=torch.float)
        return x[2, :, :, :, 0, 0]




func = Model().to('cuda')



x = torch.randn(5, 5, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
too many indices for tensor of dimension 5

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., size=(3, 5, 5, 5, 5), dtype=torch.float64), (2, slice(None, None, None), slice(None, None, None), slice(None, None, None), 0, 0)), **{}):
too many indices for tensor of dimension 5

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''