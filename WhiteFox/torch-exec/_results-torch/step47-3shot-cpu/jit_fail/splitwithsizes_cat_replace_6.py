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
        self.features = torch.nn.BatchNorm2d(64, affine=False, track_running_stats=False)

    def forward(self, v1):
        split_tensors1 = torch.split(v1, [1, 1, 1, 1, 1, 1], dim=1)
        split_tensors2 = torch.split(torch.cat([split_tensors1[i] for i in range(len(split_tensors1))], dim=1), [1, 1], dim=1)
        concatenated_tensor1 = torch.cat([split_tensors2[i] for i in range(len(split_tensors2))], dim=1)
        return concatenated_tensor1



func = Model().to('cpu')


x1 = torch.randn(1, 6, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 6 (input tensor's size at dimension 1), but got split_sizes=[1, 1]

jit:
Failed running call_function <function split at 0x7983f11faf70>(*(FakeTensor(..., size=(1, 6, s1, s2)), [1, 1]), **{'dim': 1}):
Split sizes add up to 2 but got the tensor's size of 6

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''