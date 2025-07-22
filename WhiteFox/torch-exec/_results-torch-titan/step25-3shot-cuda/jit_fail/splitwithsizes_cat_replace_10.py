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
        self.features = torch.nn.Sequential(torch.nn.MaxPool2d(2, 2, 0), torch.nn.AvgPool2d(3, 2, 2, ceil_mode=False), torch.nn.MaxPool2d(3, 2, 1))

    def forward(self, v1):
        split_tensors_1 = torch.split(v1, [1, 1], dim=1)
        concatenated_tensor_1 = torch.cat(split_tensors_1, dim=1)
        split_tensors_2 = torch.split(concatenated_tensor_1, [1, 1], dim=1)
        concatenated_tensor_2 = torch.cat(split_tensors_2, dim=1)
        return (concatenated_tensor_2, torch.split(v1, [1, 1], dim=1))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 3 (input tensor's size at dimension 1), but got split_sizes=[1, 1]

jit:
Failed running call_function <function split at 0x70d33a1b00d0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), [1, 1]), **{'dim': 1}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''