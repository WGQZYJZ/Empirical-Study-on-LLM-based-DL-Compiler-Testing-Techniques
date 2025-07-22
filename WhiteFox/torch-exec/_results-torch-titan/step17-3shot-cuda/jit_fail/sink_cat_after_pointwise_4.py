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
        self.a = torch.randn(3)
        self.b = torch.randn(4)

    def forward(self, x):
        y = torch.cat((self.a.unsqueeze((- 1)).expand((- 1), x.shape[1]), self.b.unsqueeze(0).expand(x.shape[0], (- 1))), dim=1)
        return y




func = Model().to('cuda')



x = torch.randn(2, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 3 but got size 2 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x79eed08699e0>(*((FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., device='cuda:0', size=(2, 4))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 3 but got 2 for tensor number 1 in the list

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''