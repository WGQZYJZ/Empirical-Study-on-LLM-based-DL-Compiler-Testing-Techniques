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
        self.features = torch.nn.Sequential(torch.nn.MaxPool2d(12, 8, 6, 1), torch.nn.MaxPool2d(10, 8, 5, 3), torch.nn.MaxPool2d(6, 7, 4, 2))
        self.split = torch.nn.Sequential(torch.nn.MaxPool2d(6, 5, 3, 1), torch.nn.MaxPool2d(3, 4, 2, 0), torch.nn.MaxPool2d(6, 2, 3, 1), torch.nn.MaxPool2d(3, 1, 2, 0), torch.nn.MaxPool2d(7, 7, 4, 0), torch.nn.MaxPool2d(6, 3, 5, 3), torch.nn.MaxPool2d(12, 4, 7, 0), torch.nn.MaxPool2d(4, 1, 4, 1), torch.nn.MaxPool2d(5, 5, 7, 2), torch.nn.MaxPool2d(6, 2, 6, 2), torch.nn.MaxPool2d(2, 2, 2, 1))
        self.flatten = torch.nn.Flatten()

    def forward(self, x1):
        v1 = self.features(x1)
        v2 = self.features(x1)
        concat_tensor = torch.cat([v1, v2], dim=(- 1))
        split_tensors = torch.split(concat_tensor, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return self.flatten(concatenated_tensor)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size: (3x9x9). Calculated output size: (3x-1x-1). Output size is too small

jit:
Failed running call_module L__self___features_1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 9, 9)),), **{}):
Given input size: (3x9x9). Calculated output size: (3x-1x-1). Output size is too small

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''