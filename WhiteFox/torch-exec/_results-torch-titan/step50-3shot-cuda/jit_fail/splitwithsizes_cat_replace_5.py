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
        self.features = torch.nn.BatchNorm2d(32, affine=False, track_running_stats=True)

    def forward(self, v0):
        split_tensors = torch.split(v0, [1, 1, 1], dim=1)
        split_tensor_1 = split_tensors[0]
        return (torch.cat([v0, split_tensor_1]), torch.split(v0, [1, 1, 1], dim=1))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 3 but got size 1 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7403434699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64))],), **{}):
Sizes of tensors must match except in dimension 0. Expected 3 but got 1 for tensor number 1 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''