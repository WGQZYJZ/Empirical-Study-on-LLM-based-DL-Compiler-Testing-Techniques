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
        self.features = torch.nn.Linear(3, 32)

    def forward(self, v1):
        concatenated_tensor = torch.cat(torch.split(v1, torch.tensor([1, 2]), dim=1), dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 2], dim=1))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes(): argument 'split_sizes' (position 2) must be tuple of ints, not Tensor

jit:
Failed running call_function <function split at 0x7b1323eef0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., size=(2,), dtype=torch.int64)), **{'dim': 1}):
split_with_sizes(): argument 'split_sizes' (position 2) must be tuple of ints, not FakeTensor

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''