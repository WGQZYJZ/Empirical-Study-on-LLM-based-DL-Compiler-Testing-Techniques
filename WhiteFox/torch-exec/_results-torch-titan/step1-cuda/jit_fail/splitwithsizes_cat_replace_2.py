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

    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim

    def forward(self, x):
        split_sizes = [3, 2, 5]
        parts = torch.split(x, split_sizes, self.dim)
        dim = self.dim
        xcat = []
        for i in range(len(parts)):
            xcat.append(parts[((i - 1) - (2 * i))])
        xcat = torch.cat(xcat, dim=dim)
        return xcat



func = Model().to('cuda')



x = torch.randn(20, 5, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 5 (input tensor's size at dimension 1), but got split_sizes=[3, 2, 5]

jit:
Failed running call_function <function split at 0x752207bb00d0>(*(FakeTensor(..., device='cuda:0', size=(20, 5, 64, 64)), [3, 2, 5], 1), **{}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''