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



class Layer1(torch.nn.Module):

    def __init__(self, inp, hidden, out):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(inp, 32, 3, 1, 1, bias=False)
        self.bn1 = torch.nn.BatchNorm2d(32, affine=False, track_running_stats=False)

    def forward(self, v1):
        return torch.nn.ReLU()(self.bn1(self.conv1(v1)))




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.features = Layer1(3, 16, 32)
        self.extra = torch.nn.ReLU()

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=3)
        concatenated_tensor = torch.cat(split_tensors, dim=3)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=3))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 64 (input tensor's size at dimension 3), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x777a2186f0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), [1, 1, 1]), **{'dim': 3}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''