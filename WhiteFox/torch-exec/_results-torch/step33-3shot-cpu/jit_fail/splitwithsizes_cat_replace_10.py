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
        self.features = torch.nn.ModuleList([torch.nn.Conv1d(1, 1, kernel_size=2), torch.nn.BatchNorm1d(1)])

    def forward(self, x):
        split_tensors = torch.split(x, [2], dim=0)
        x1 = torch.cat([split_tensors[0], split_tensors[1], split_tensors[3], split_tensors[4]], dim=0)
        return x1



func = Model().to('cpu')


x = torch.randn(8, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 8 (input tensor's size at dimension 0), but got split_sizes=[2]

jit:
Failed running call_function <function split at 0x748dfeffcf70>(*(FakeTensor(..., size=(8, 1)), [2]), **{'dim': 0}):
Split sizes add up to 2 but got the tensor's size of 8

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''