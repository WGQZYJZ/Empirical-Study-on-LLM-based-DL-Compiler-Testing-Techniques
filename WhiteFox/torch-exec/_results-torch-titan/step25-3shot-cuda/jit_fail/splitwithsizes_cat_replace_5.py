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
        self.relu = torch.nn.ReLU()
        self.conv2d_1 = torch.nn.Conv2d(3, 32, 3, 1, 1)
        self.conv2d_2 = torch.nn.Conv2d(32, 64, 3, 1, 1)

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=2)
        concatenated_tensor = torch.cat(self.conv2d_2(self.relu(self.conv2d_1(split_tensors[0].squeeze(dim=2)))), dim=2)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=2))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 64 (input tensor's size at dimension 2), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x70d33a1b00d0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), [1, 1, 1]), **{'dim': 2}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''