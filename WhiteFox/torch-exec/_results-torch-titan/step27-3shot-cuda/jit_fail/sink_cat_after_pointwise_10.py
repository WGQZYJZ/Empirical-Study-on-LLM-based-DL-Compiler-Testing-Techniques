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
        x = torch.cat((torch.cat((x, x), dim=1), x), dim=0)
        x = x.transpose(1, 0).view((- 1), (x.shape[2:] * 4))
        return x




func = Model().to('cuda')



x = torch.randn(3, 4, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 8 but got size 4 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x75ab5be699e0>(*((FakeTensor(..., device='cuda:0', size=(3, 8, 3)), FakeTensor(..., device='cuda:0', size=(3, 4, 3))),), **{'dim': 0}):
Sizes of tensors must match except in dimension 0. Expected 8 but got 4 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''