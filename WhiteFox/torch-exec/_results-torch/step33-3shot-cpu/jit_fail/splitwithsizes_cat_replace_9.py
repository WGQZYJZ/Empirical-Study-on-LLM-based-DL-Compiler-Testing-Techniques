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
        self.features = torch.nn.ModuleList([torch.nn.Conv2d(3, 32, 1, 1, 0)])

    def forward(self, v1):
        split_tensor = torch.split(v1, [1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensor, dim=1)
        return (concatenated_tensor,)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 3 (input tensor's size at dimension 1), but got split_sizes=[1, 1]

jit:
Failed running call_function <function split at 0x748dfeffcf70>(*(FakeTensor(..., size=(1, 3, 64, 64)), [1, 1]), **{'dim': 1}):
Split sizes add up to 2 but got the tensor's size of 3

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''