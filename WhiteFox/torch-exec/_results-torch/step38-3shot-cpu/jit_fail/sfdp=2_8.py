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

    def __init__(self, n_head=8):
        super().__init__()
        self.n_head = n_head

    def forward(self, q, k, v, inv_scale_factor=1, dropout_p=0.2):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor ** 0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model(n_head=8).to('cpu')


input_tensor = torch.randn(1, 64, 200)

q = torch.randn(1, 8, 64)

k = torch.randn(1, 8, 200)

v = torch.randn(1, 8, 200)

test_inputs = [input_tensor, q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 200] but got: [1, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x73e4f4996ec0>(*(FakeTensor(..., size=(1, 64, 200)), FakeTensor(..., size=(1, 64, 8))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 200] but got: [1, 64].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''