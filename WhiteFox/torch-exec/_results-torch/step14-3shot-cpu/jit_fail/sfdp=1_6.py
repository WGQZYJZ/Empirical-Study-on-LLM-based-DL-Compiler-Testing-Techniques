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
        self.weight = torch.rand((24, 24))

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        inv_scale_factor = torch.rsqrt(torch.float32.max).to(x1.device)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(self.weight)
        return output


func = Model().to('cpu')


x1 = torch.randn(5, 24, 2)

x2 = torch.randn(5, 2, 24)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [5, 2] but got: [5, 24].

jit:
Failed running call_function <built-in method matmul of type object at 0x7f7963796ec0>(*(FakeTensor(..., size=(s0, s4, s5)), FakeTensor(..., size=(s0, s2, s1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0, s5] but got: [s0, s2].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''