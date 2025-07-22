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
        t1 = torch.mm(x2, x1)
        v2 = torch.mm(x1, x2)
        t2 = torch.cat([v2, v2], 0)
        return torch.cat([v2, v2, t2, t2, t2, t2], 1)




func = Model().to('cuda')



x1 = torch.randn(8, 2)



x2 = torch.randn(2, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 8 but got size 16 for tensor number 2 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7385996699e0>(*([FakeTensor(..., device='cuda:0', size=(8, 8)), FakeTensor(..., device='cuda:0', size=(8, 8)), FakeTensor(..., device='cuda:0', size=(16, 8)), FakeTensor(..., device='cuda:0', size=(16, 8)), FakeTensor(..., device='cuda:0', size=(16, 8)), FakeTensor(..., device='cuda:0', size=(16, 8))], 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 8 but got 16 for tensor number 2 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''