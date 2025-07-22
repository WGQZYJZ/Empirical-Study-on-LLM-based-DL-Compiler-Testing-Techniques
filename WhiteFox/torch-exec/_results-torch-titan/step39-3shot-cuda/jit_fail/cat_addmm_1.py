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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 8)

    def forward(self, x):
        x = self.layers(x)
        x = torch.stack((x, x, x, x, x, x, x, x), dim=1)
        x = torch.cat((x[:, 3:].unsqueeze(0).repeat_interleave(2, dim=0), x[:, 0:3].unsqueeze(0).repeat_interleave(2, dim=0)), dim=0)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 5 but got size 3 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7de9f3e699e0>(*((FakeTensor(..., device='cuda:0', size=(2, 2, 5, 8)), FakeTensor(..., device='cuda:0', size=(2, 2, 3, 8))),), **{'dim': 0}):
Sizes of tensors must match except in dimension 0. Expected 5 but got 3 for tensor number 1 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''