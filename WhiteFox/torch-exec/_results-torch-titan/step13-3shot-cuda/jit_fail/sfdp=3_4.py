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
        self.key = Parameter(torch.Tensor(8, 8, 16, 16))
        self.scale_factor = 10.0
        self.dropout_p = 0.1
        self.value = torch.nn.Parameter(torch.Tensor(8, 8, 16, 16))

    def forward(self, x1):
        k = self.key
        v = self.value
        s = self.scale_factor
        p = self.dropout_p
        _1 = torch.matmul(x1, k.transpose((- 2), (- 1)))
        _2 = (_1 * s)
        _3 = _2.softmax(dim=(- 1))
        _4 = torch.nn.functional.dropout(_3, p=p)
        _5 = _4.matmul(v)
        return _5



func = Model().to('cuda')



s = 4


s = 4


x1 = torch.randn(1, 8, s, s)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [64, 4] but got: [64, 16].

jit:
Failed running call_function <built-in method matmul of type object at 0x7043d04699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 4, 4)), FakeTensor(..., device='cuda:0', size=(8, 8, 16, 16), requires_grad=True)), **{}):
Expected size for first two dimensions of batch2 tensor to be: [64, 4] but got: [64, 16].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''