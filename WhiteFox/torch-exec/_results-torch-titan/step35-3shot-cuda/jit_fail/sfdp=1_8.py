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
        self.query = torch.nn.Parameter(torch.empty(4, 4, 64, 64))
        inq = torch.randn(4, 4, 64, 64)
        torch.nn.init.kaiming_uniform_(self.query, a=math.sqrt(5))
        self.padding = torch.nn.ConstantPad2d(1, (- 1000000000.0))
        self.value = torch.nn.Parameter(torch.empty(64, 32, 64, 64))
        inv = torch.randn(64, 32, 64, 64)
        torch.nn.init.kaiming_normal_(self.value, a=math.sqrt(5))

    def forward(self, x1):
        q = torch.matmul(self.query, x1.transpose((- 2), (- 1)))
        s1 = q.div(32)
        w1 = torch.nn.functional.softmax(s1, dim=(- 1))
        d1 = torch.nn.functional.dropout(w1, 0.2)
        v = torch.matmul(d1, self.value.transpose((- 2), (- 1)))
        return v



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7272dc8699e0>(*(Parameter(FakeTensor(..., device='cuda:0', size=(4, 4, 64, 64), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''