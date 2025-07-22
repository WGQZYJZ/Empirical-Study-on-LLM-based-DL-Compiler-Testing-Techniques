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
        self.key_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.value_conv = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)

    def forward(self, x1):
        x2 = self.key_conv(x1)
        x3 = self.value_conv(x1)
        v4 = torch.matmul(x2, x3.transpose(-2, -1))
        v5 = v4.div(0.12)
        v6 = v5.softmax(dim=-1)
        v7 = torch.nn.functional.dropout(v6, p=0.1, training=False)
        v8 = torch.matmul(v7, x3)
        return v8


func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7378acf96ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), FakeTensor(..., device='cuda:0', size=(1, 4, 66, 66))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''