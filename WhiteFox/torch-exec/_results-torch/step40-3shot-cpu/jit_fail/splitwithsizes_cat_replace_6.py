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
        self.features = torch.nn.Sequential(torch.nn.ReLU(inplace=True), torch.nn.ConvTranspose2d(4, 8, 5, 5, 0, 0, bias=False))

    def forward(self, v1):
        split_tensors = torch.split(v1, (1, 1, 1), dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, (1, 1, 1), dim=1))



func = Model().to('cpu')


x1 = torch.randn(1, 4, 3, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 4 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x72e03237af70>(*(FakeTensor(..., size=(1, s0, s1, s2)), (1, 1, 1)), **{'dim': 1}):
Split sizes add up to 3 but got the tensor's size of s0

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''