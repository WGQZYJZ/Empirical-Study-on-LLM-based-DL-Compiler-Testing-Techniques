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

    def forward(self, x):
        t1 = x.view(1, (- 1))
        t2 = x.view(2, (- 1))
        t3 = torch.cat((t1, t2), dim=0)
        t4 = t3.tanh()
        t5 = t4.relu()
        return t5




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 24 but got size 12 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7af1aaa699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 24)), FakeTensor(..., device='cuda:0', size=(2, 12))),), **{'dim': 0}):
Sizes of tensors must match except in dimension 0. Expected 24 but got 12 for tensor number 1 in the list

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''