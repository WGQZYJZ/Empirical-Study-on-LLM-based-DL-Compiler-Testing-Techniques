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
        self.proj = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.out_proj = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0)

    def forward(self, x1, x2):
        v1 = self.proj(x1)
        v2 = torch.matmul(v1, x2.transpose((- 2), (- 1)))
        v3 = v2.div(1e-06)
        v4 = v3.softmax(dim=(- 1))
        v5 = F.dropout(v4, p=0.5)
        v6 = torch.matmul(v5, x2)
        v7 = self.out_proj(v6)
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 1, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 66] but got: [8, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x7005396699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 66] but got: [8, 64].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''