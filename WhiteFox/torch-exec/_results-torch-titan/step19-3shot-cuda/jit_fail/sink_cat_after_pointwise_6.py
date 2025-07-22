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
        x3 = torch.cat((x1, x2), dim=1)
        x3 = torch.relu(x3)
        return (x3 if (x1.shape[0] == 1) else x3.view((- 1)))




func = Model().to('cuda')



x1 = torch.randn(2, 3)



x2 = torch.randn(3, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 2 but got size 3 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7efc634699e0>(*((FakeTensor(..., device='cuda:0', size=(2, 3)), FakeTensor(..., device='cuda:0', size=(3, 3))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 2 but got 3 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''