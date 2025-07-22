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

    def forward(self, x1):
        v1 = torch.mean(x1, dim=(1, 2, 3))
        t1 = torch.nn.functional.softmax(v1, dim=(- 1))
        t2 = torch.unsqueeze(t1, dim=1)
        t3 = torch.unsqueeze(t1, dim=2)
        t4 = torch.unsqueeze(t1, dim=3)
        t5 = ((t2 * t3) * t4)
        t6 = torch.transpose(t5, dim0=1, dim1=2)
        t7 = torch.transpose(t6, dim0=2, dim1=3)
        t8 = (t7 - t5)
        z9 = (t1 - 0.5)
        f10 = (t8 + z9)
        return f10




func = Model().to('cuda')



x1 = torch.randn(1, 8, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-2, 1], but got 2)

jit:
Failed running call_function <built-in method unsqueeze of type object at 0x74ee764699e0>(*(FakeTensor(..., device='cuda:0', size=(1,)),), **{'dim': 2}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''