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

    def forward(self, x1):
        v1 = torch.cat([x1, x1])
        v2 = v1[:, None, :, :, None]
        v3 = v2[0, :, :, None]
        v4 = [v1, v3]
        v5 = torch.cat(v4, 2)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 5, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 5 and 7

jit:
Failed running call_function <built-in method cat of type object at 0x79c37aa699e0>(*([FakeTensor(..., device='cuda:0', size=(2, 5, 3, 224, 224)), FakeTensor(..., device='cuda:0', size=(1, 5, 1, 3, 1, 224, 224))], 2), **{}):
Sizes of tensors must match except in dimension 2. Expected 2 but got 1 for tensor number 1 in the list

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''