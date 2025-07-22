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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 3, 3, 1, 1), torch.nn.Conv2d(3, 12, 3, 1, 1))
        self.split_1 = torch.nn.Sequential(torch.nn.Conv2d(3, 1, 3, 1, 1))
        self.split_2 = torch.nn.Sequential(torch.nn.Conv2d(12, 1, 3, 1, 1))
        self.split_3 = torch.nn.Sequential(torch.nn.Conv2d(3, 1, 3, 1, 1))
        self.split_4 = torch.nn.Sequential(torch.nn.Conv2d(12, 1, 3, 1, 1))

    def forward(self, x1):
        v1 = self.features(x1)
        split_tensors_1 = torch.split(v1, [1, 1, 1], dim=1)
        split_tensors_2 = torch.split(v1, [1, 1, 1], dim=1)
        split_tensors_3 = torch.split(v1, [1, 1, 1], dim=1)
        split_tensors_4 = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors_1, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 12 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x7502d2b7cf70>(*(FakeTensor(..., size=(1, 12, 64, 64)), [1, 1, 1]), **{'dim': 1}):
Split sizes add up to 3 but got the tensor's size of 12

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''