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
        self.conv = torch.nn.Conv2d(3, 8, 7, stride=1, padding=4)

    def forward(self, x1, padding1=False, padding2=torch.randint((- 2), 3, [3, 7, 7]), padding3=2):
        v1 = self.conv(x1)
        v2 = (v1 + 2)
        t3 = torch.randint(0, 3, [3, 7, 7])
        v3 = (v2 * t3)
        t4 = torch.randint(0, 3, [3, 7, 7])
        v4 = (v3 + t4)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 124, 124)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (126) must match the size of tensor b (7) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 126, 126)), FakeTensor(..., size=(3, 7, 7), dtype=torch.int64)), **{}):
Attempting to broadcast a dimension of length 7 at -1! Mismatching argument at index 1 had torch.Size([3, 7, 7]); but expected shape should be broadcastable to [1, 8, 126, 126]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''