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



class my_cat(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), dim=1)
        v2 = torch.cat((x2, x1), dim=1)
        v4 = torch.cat((v1, v2), dim=1)
        v4 = torch.sigmoid(v4)
        m = v4.argmax(dim=0)
        m = m.reshape(2, (- 1))
        n = torch.cat((v1, m), dim=0)
        n = n.T[2:]
        return n.T




func = my_cat().to('cuda')



x1 = torch.randn(2, 4, 5)



x2 = torch.randn(2, 4, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 5 but got size 3 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7b4bd64699e0>(*((FakeTensor(..., device='cuda:0', size=(2, 4, 5)), FakeTensor(..., device='cuda:0', size=(2, 4, 3))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 5 but got 3 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''