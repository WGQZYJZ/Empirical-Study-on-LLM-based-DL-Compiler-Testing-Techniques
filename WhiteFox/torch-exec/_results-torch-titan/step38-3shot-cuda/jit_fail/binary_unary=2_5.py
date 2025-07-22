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
        self.conv = torch.nn.Conv2d(1, 8, 1, stride=2)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = (v1 - x2)
        v3 = F.relu(v2)
        v4 = F.relu((x1 - self.conv(x2)))
        v5 = v4.flatten(1)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 5, 5)



x2 = torch.randn(1, 1, 4, 4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 3, 3)), FakeTensor(..., device='cuda:0', size=(1, 1, 4, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 4, 4]); but expected shape should be broadcastable to [1, 8, 3, 3]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''