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
        (t0, t1, t2, t3) = torch.split(x, [4, 2, 2, 1], 1)
        t4 = torch.cat((t0, t1), 1)
        t5 = torch.cat((t2, t3), 1)
        t6 = torch.cat((t4, t5), 1)
        return t6



func = Model().to('cuda')



x = torch.randn(1, 6, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 6 (input tensor's size at dimension 1), but got split_sizes=[4, 2, 2, 1]

jit:
Failed running call_function <function split at 0x757d0f9700d0>(*(FakeTensor(..., device='cuda:0', size=(1, 6, 4, 4)), [4, 2, 2, 1], 1), **{}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''