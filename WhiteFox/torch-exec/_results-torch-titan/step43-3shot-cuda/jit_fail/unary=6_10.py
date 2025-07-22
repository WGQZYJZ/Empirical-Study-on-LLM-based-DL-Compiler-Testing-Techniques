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
        self.conv1 = torch.nn.Conv2d(3, 32, kernel_size=(1, 3), stride=(1, 1), padding=0, dilation=1)

    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = t1.sum((2, 3))
        t3 = (t2 + 3)
        t4 = torch.clamp_min(t3, 0)
        t5 = torch.clamp_max(t4, 6)
        t6 = (t1 * t5)
        t7 = (t6 / 6)
        return t7




func = Model().to('cuda')



x1 = torch.randn(2, 3, 120, 120)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (118) must match the size of tensor b (32) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(2, 32, 120, 118)), FakeTensor(..., device='cuda:0', size=(2, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([2, 32]); but expected shape should be broadcastable to [2, 32, 120, 118]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''