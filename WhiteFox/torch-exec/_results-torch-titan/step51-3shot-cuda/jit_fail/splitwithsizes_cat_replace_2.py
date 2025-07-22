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

    def forward(self, v1, v2):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat((split_tensors[0], v2, split_tensors[1]), dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 1, 32, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 64 but got size 32 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x713c38c699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 1, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 64 but got 32 for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''