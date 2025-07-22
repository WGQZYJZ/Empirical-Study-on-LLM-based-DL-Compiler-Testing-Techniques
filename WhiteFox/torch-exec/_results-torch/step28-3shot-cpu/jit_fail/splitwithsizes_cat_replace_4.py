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
        self.conv = torch.nn.Conv2d(3, 32, 3, 1, 1)

    def forward(self, v1, v2, v3, v4):
        split_tensors = torch.split(self.conv(v1), [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat([self.conv(v2), self.conv(v3), self.conv(v4)], dim=1)
        f = torch.sigmoid(concatenated_tensor + torch.sigmoid(split_tensors[0]) + torch.sigmoid(split_tensors[1]) + torch.sigmoid(split_tensors[2]))
        return (concatenated_tensor, split_tensors, f)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

x3 = torch.randn(1, 3, 64, 64)

x4 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 32 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x789879b3bf70>(*(FakeTensor(..., size=(1, 32, 64, 64)), [1, 1, 1]), **{'dim': 1}):
Split sizes add up to 3 but got the tensor's size of 32

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''