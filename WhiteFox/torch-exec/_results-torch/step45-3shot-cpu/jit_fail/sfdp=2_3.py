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

    def forward(self, q, k, v, d):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


d = 128
q = torch.randn(1, d, 512)

d = 128
k = torch.randn(1, d, 495)

d = 128
v = torch.randn(1, d, 495)
d = 1

test_inputs = [q, k, v, d]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 512] but got: [1, 495].

jit:
Failed running call_function <built-in method matmul of type object at 0x75b0e3f96ec0>(*(FakeTensor(..., size=(1, 128, 512)), FakeTensor(..., size=(1, 495, 128))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 512] but got: [1, 495].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''