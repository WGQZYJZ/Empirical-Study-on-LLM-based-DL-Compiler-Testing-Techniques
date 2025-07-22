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
        self.features = torch.nn.ModuleList([torch.nn.Conv2d(3, 32, 3, 1, 1)])

    def forward(self, v2):
        split_tensors = torch.split(v2, [1, 1, 1], dim=3)
        concatenated_tensor = torch.cat(split_tensors, dim=3)
        return (concatenated_tensor, torch.split(v2, [1, 1, 1], dim=3))




func = Model().to('cuda')



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 64 (input tensor's size at dimension 3), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x74f0ed2700d0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), [1, 1, 1]), **{'dim': 3}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''