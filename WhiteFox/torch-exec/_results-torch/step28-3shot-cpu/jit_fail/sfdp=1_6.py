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

    def forward(self, q, k, v, inv_scale_factor, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


q = torch.randn(1, 1, 768)

k = torch.randn(64, 1, 64)

v = torch.randn(64, 1, 64)

inv_scale_factor = torch.randn(1)
dropout_p = 1

test_inputs = [q, k, v, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [64, 768] but got: [64, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x76d8cf196ec0>(*(FakeTensor(..., size=(1, 1, 768)), FakeTensor(..., size=(64, 64, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [64, 768] but got: [64, 64].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''