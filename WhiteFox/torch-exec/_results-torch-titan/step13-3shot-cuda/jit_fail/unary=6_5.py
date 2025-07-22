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



class M1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=3)

    def forward(self, x1):
        e1 = self.conv1(x1)
        e2 = (e1 + 3)
        e3 = torch.clamp(e2, 0, 6)
        e4 = torch.cat([e1, e2, e3], 1)
        e5 = torch.sigmoid(((e1 * e4) + 8))
        e6 = (e1 + e4)
        e7 = ((e6 + e5) + 3)
        e8 = (e6 + e7)
        return (e5 + e8)




func = M1().to('cuda')



x1 = torch.zeros(2, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (24) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(2, 8, 68, 68)), FakeTensor(..., device='cuda:0', size=(2, 24, 68, 68))), **{}):
Attempting to broadcast a dimension of length 24 at -3! Mismatching argument at index 1 had torch.Size([2, 24, 68, 68]); but expected shape should be broadcastable to [2, 8, 68, 68]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''