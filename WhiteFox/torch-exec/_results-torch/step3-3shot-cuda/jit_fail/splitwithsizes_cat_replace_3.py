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
        v1 = x1.clone()
        (v2, v3, v4, v5) = torch.split(v1, [1, 2, 3, 4], dim=1)
        return True


func = Model().to('cuda')


x1 = torch.randn(1, 8, 8, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 8 (input tensor's size at dimension 1), but got split_sizes=[1, 2, 3, 4]

jit:
Failed running call_function <function split at 0x74d6583fbf70>(*(FakeTensor(..., device='cuda:0', size=(1, 8, s0, s1)), [1, 2, 3, 4]), **{'dim': 1}):
Split sizes add up to 10 but got the tensor's size of 8

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''