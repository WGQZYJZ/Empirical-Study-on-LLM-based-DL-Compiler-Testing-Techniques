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

    def __init__(self, **kwargs):
        super().__init__()
        scale_factor = torch.tensor(kwargs.pop('scale_factor', 1.0))
        dropout_p = kwargs.pop('dropout_p', 0.0)
        self.dropout_p = dropout_p
        self.scale_factor = scale_factor

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scale_factor = self.scale_factor.to(xk.device) if self.scale_factor.is_floating_point() else self.scale_factor
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk * k


func = Model().to('cpu')


x1 = torch.randn(3, 4, 5)

x2 = torch.rand(2, 4, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x7bed07996ec0>(*(FakeTensor(..., size=(3, 4, 5)), FakeTensor(..., size=(2, 5, 4))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''