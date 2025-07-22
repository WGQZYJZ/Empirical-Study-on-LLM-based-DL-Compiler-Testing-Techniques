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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(32, 32, 3, 2, 1), torch.nn.Conv2d(32, 3, 1, 1, 0))
        self.split = torch.nn.Sequential(torch.nn.Conv2d(32, 32, 1, 1, 0))

    def forward(self, x1):
        v1 = self.features(x1)
        split_tensors = torch.split(v1, [1, 1, 1], dim=2)
        concatenated_tensor = torch.cat(split_tensors, dim=2)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=2))




func = Model().to('cuda')



x1 = torch.randn(1, 32, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 32 (input tensor's size at dimension 2), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x76c9a006e0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32)), [1, 1, 1]), **{'dim': 2}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''