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

    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        inv_scale_factor = 1.0 / 32768
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        p = 0.2
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=p)
        output = dropout_qk.matmul(x3)
        return output


func = Model().to('cpu')


x1 = torch.randn(2, 8, 64)

x2 = torch.randn(2, 8, 64)

x3 = torch.randn(2, 64, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 8] but got: [2, 64].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(2, s4, s1)), FakeTensor(..., size=(2, 64, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, s1] but got: [2, 64].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''