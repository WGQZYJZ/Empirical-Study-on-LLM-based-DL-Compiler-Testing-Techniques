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

    def forward(self, x1, x2):
        t = torch.cat([x1, x2, x2], dim=1)
        d = t.view(t.shape[0], (- 1))
        c = d.clamp(0, 10, 4)
        x = (x1 if ((c.shape == (1, 17)) or (c.shape == (1, 21))) else x2)
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 1, 1, 3, 5, 7)



x2 = torch.randn(1, 1, 2, 4, 6)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 6 and 5

jit:
Failed running call_function <built-in method cat of type object at 0x7d2e1d8699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 1, 1, 3, 5, 7)), FakeTensor(..., device='cuda:0', size=(1, 1, 2, 4, 6)), FakeTensor(..., device='cuda:0', size=(1, 1, 2, 4, 6))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 1 but got 2 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''