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
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x):
        a = x.shape
        b = a[(- 1)]
        v1 = x.new_zeros((a[:(- 1)] + ((b - 1),)))
        v2 = torch.cat((x, v1), dim=(- 1))
        y = torch.stack(v1, dim=(- 1)).flatten()
        return torch.nn.functional.relu(y)




func = Model().to('cuda')



x = torch.randn(1, 5, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
stack(): argument 'tensors' (position 1) must be tuple of Tensors, not Tensor

jit:
Failed running call_function <built-in method stack of type object at 0x7321f70699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 2)),), **{'dim': -1}):
stack(): argument 'tensors' (position 1) must be tuple of Tensors, not FakeTensor

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''