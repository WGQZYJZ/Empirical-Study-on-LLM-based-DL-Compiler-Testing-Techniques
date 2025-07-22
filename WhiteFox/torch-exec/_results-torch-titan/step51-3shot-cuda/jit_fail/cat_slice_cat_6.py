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

    def forward(self, x0, x1):
        v0 = torch.cat([x0, x1], dim=0)
        v1 = v0[:, :18446744073709551615]
        v2 = v1[:, :18446744073709551615]
        v3 = torch.cat([v0, v2], dim=1)
        return v3



func = Model().to('cuda')



x0 = torch.randn(2, 1024)



x1 = torch.randn(2, 192)


test_inputs = [x0, x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 1024 but got size 192 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x779e520699e0>(*([FakeTensor(..., device='cuda:0', size=(2, 1024)), FakeTensor(..., device='cuda:0', size=(2, 192))],), **{'dim': 0}):
Sizes of tensors must match except in dimension 0. Expected 1024 but got 192 for tensor number 1 in the list

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''