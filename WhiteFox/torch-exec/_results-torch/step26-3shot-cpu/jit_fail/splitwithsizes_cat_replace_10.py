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
        self.softmax = torch.nn.Sequential(torch.nn.Conv2d(59, 2, 1, stride=1), torch.nn.Softmax(dim=1))
        self.resnet = torch.nn.Sequential(torch.nn.Conv2d(2, 9, 5, 1, 4), torch.nn.Conv2d(9, 4, 5), torch.nn.Conv2d(4, 4, 5), torch.nn.Conv2d(4, 1, 1), torch.nn.Softmax(dim=1))

    def forward(self, v1):
        split_tensors = torch.split(v1, [2, 2, 2, 2, 2, 2, 2, 2, 2], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [2, 2, 2, 2, 2, 2, 2, 2, 2], dim=1))



func = Model().to('cpu')


x1 = torch.randn(1, 59, 7, 7)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 59 (input tensor's size at dimension 1), but got split_sizes=[2, 2, 2, 2, 2, 2, 2, 2, 2]

jit:
Failed running call_function <function split at 0x7c5e8cd3bf70>(*(FakeTensor(..., size=(1, 59, 7, 7)), [2, 2, 2, 2, 2, 2, 2, 2, 2]), **{'dim': 1}):
Split sizes add up to 18 but got the tensor's size of 59

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''