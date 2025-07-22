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
        self.features = torch.nn.Sequential(torch.nn.Linear(3, 8), torch.nn.Sigmoid())
        self.pad = torch.nn.Sequential(torch.nn.ConstantPad1d(3, value=0.0))

    def forward(self, x0):
        x4 = self.features(x0)
        x0 = self.pad(x0)
        split_tensors = torch.split(x0, [1, 1, 1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(x0, [1, 1, 1, 1, 1], dim=1))




func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 9 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1, 1, 1]

jit:
Failed running call_function <function split at 0x7e713a4ad0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 9)), [1, 1, 1, 1, 1]), **{'dim': 1}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''