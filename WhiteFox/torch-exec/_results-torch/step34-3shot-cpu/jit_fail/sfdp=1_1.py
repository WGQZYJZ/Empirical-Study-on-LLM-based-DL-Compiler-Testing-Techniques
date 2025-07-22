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

    def forward(self, x1):
        qk = x1.transpose(1, 2).matmul(x1)
        inv_scale_factor = (5000.0 / qk.size(1)) ** 0.5
        scaled_qk = qk / inv_scale_factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        out = dropout_qk.matmul(x1).transpose(1, 2)
        return out


func = Model().to('cpu')


x1 = torch.randn(1, 64, 50)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 50] but got: [1, 64].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(1, 50, 50)), FakeTensor(..., size=(1, 64, 50))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 50] but got: [1, 64].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''