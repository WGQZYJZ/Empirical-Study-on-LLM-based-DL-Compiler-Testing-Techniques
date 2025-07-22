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

    def forward(self, x1, x2, x3, x4):
        t1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        t2 = (t1 * 1.7071067811865477)
        t3 = torch.nn.functional.softmax(t2, dim=(- 1))
        t4 = torch.nn.functional.dropout(t3, p=0.10000000149011612)
        t5 = torch.matmul(t3, x3)
        t6 = torch.matmul(t4, x4)
        concat = torch.cat([t5, t6], dim=0)
        return concat



func = Model().to('cuda')



x1 = torch.randn(1, 4)



x2 = torch.randn(1, 4)



x3 = torch.randn(1, 8)



x4 = torch.randn(1, 16)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 8 but got size 16 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x701cc6e699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 8)), FakeTensor(..., device='cuda:0', size=(1, 16))],), **{'dim': 0}):
Sizes of tensors must match except in dimension 0. Expected 8 but got 16 for tensor number 1 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''