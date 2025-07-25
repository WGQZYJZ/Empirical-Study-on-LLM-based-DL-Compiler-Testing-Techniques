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
        (v1, v2, v3) = torch.split(x, (8, 8, 8))
        return torch.cat([v1, v2, v3], dim=1)



func = Model().to('cuda')



x = torch.randn(1, 28, 40, 40)


test_inputs = [x]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 1 (input tensor's size at dimension 0), but got split_sizes=[8, 8, 8]

jit:
Failed running call_function <function split at 0x7a6eca16f0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 28, 40, 40)), (8, 8, 8)), **{}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''