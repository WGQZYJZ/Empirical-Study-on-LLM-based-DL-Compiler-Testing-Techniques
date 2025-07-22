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
        self.convs = torch.nn.Sequential(torch.nn.Conv2d(3, 10, 3, 1, 1), torch.nn.Dropout2d())
        self.features = torch.nn.Sequential(torch.nn.Conv2d(10, 10, 3, 1, 1), torch.nn.Conv2d(10, 10, 3, 2, 3), torch.nn.Conv2d(10, 10, 3, 1, 1))
        self.split = torch.nn.Sequential(torch.nn.Conv2d(10, 10, 3, 2, 3))

    def forward(self, x):
        v1 = self.convs(x)
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))




func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 10 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x7b4bd8dae0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 10, 64, 64)), [1, 1, 1]), **{'dim': 1}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''