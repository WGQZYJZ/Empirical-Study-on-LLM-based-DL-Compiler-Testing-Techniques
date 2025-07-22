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

    def forward(self, x1):
        v1 = torch.split(x1, [2 for i in range(x1.size(1))], dim=1)
        v2 = torch.cat([v1[0], v1[1], v1[2]], dim=1)
        return (len(v2) > 0)



func = Model().to('cuda')



x1 = torch.randn(1, 14, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 14 (input tensor's size at dimension 1), but got split_sizes=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

jit:
Failed running call_function <function split at 0x7a6eca16f0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 14, 64, 64)), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), **{'dim': 1}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''