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
        self.dropout_p = 0.1
        self.dropout = torch.nn.Dropout(p=self.dropout_p)

    def forward(self, x1, x2):
        v1 = x1.matmul(x2.transpose((- 2), (- 1)))
        v2 = (v1 / self.scale_factor)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = self.dropout(v3)
        v5 = v4.matmul(x2)
        return v5



func = Model().to('cuda')



x1 = torch.randn(5, 6, 8)



x2 = torch.randn(6, 8, 7)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (6) at non-singleton dimension 0

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(5, 6, 8)), FakeTensor(..., device='cuda:0', size=(6, 7, 8))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''