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
        self.tanh1 = torch.nn.Tanh()
        self.view1 = torch.nn.Unflatten(1, (20, 2, 2))

    def forward(self, x):
        y = self.tanh1(x)
        y = self.view1(y)
        x = self.tanh1(y)
        return x



func = Model().to('cpu')


x = torch.randn(2, 20, 1, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
unflatten: Provided sizes [20, 2, 2] don't multiply up to the size of dim 1 (20) in the input tensor

jit:
Failed running call_method unflatten(*(FakeTensor(..., size=(2, 20, 1, 1)), 1, (20, 2, 2)), **{}):
unflatten: Provided sizes [20, 2, 2] don't multiply up to the size of dim 1 (20) in the input tensor

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/flatten.py", line 155, in forward
    return input.unflatten(self.dim, self.unflattened_size)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''