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

    def forward(self, query, key, value, dropout_p, inv_scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(2, 512, 15)

key = torch.randn(2, 15, 512)

value = torch.randn(2, 15, 512)
dropout_p = 1
inv_scale_factor = 1

test_inputs = [query, key, value, dropout_p, inv_scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 15] but got: [2, 512].

jit:
Failed running call_function <built-in method matmul of type object at 0x7a8252596ec0>(*(FakeTensor(..., size=(2, 512, 15)), FakeTensor(..., size=(2, 512, 15))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 15] but got: [2, 512].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''