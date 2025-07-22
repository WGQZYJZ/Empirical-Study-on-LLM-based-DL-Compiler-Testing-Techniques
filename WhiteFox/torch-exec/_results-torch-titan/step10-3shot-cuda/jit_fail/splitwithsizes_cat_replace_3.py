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
        self.features = torch.nn.Sequential(torch.nn.ReLU(inplace=False), torch.nn.Hardtanh((- 0.1), 0.1))
        self.split = torch.nn.Sequential(torch.nn.Sigmoid(), torch.nn.ReLU(inplace=True))

    def forward(self, x1):
        v1 = self.features(x1)
        split_tensors = torch.split(v1, [1, 1, 1, 1], dim=2)
        concatenated_tensor = torch.cat(split_tensors, dim=2)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1, 1], dim=2))




func = Model().to('cuda')



x1 = torch.randn(1, 4, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 16 (input tensor's size at dimension 2), but got split_sizes=[1, 1, 1, 1]

jit:
Failed running call_function <function split at 0x7c58a6eb00d0>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 16, 16)), [1, 1, 1, 1]), **{'dim': 2}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''