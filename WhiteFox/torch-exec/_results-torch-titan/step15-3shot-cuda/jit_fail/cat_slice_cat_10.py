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
        self.concat = torch.cat

    def forward(self, x1, x2):
        t1 = self.concat([x1, x2], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:64]
        t4 = self.concat([t1, t3], dim=1)
        return t4



func = Model().to('cuda')



x1 = torch.randn(1, 128, 4, 4)



x2 = torch.randn(1, 64, 8, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 4 but got size 8 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7e79a38699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 128, 4, 4)), FakeTensor(..., device='cuda:0', size=(1, 64, 8, 8))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 4 but got 8 for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''