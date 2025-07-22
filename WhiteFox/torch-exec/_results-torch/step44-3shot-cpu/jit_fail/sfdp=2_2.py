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

    def forward(self, query, key, value, dropout_p=0.5):
        qk = torch.matmul(query, key.transpose(-2, -1))
        inv_scale_factor = np.sqrt(query.shape[-1])
        scaled_qk = qk.div(inv_scale_factor)
        return torch.nn.functional.dropout(scaled_qk.softmax(dim=-1).matmul(value), p=dropout_p)


func = Model().to('cpu')


query = torch.randn(1, 8, 128)

key = torch.randn(1, 8, 256)

value = torch.randn(1, 8, 256)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 256].

jit:
Failed running call_function <built-in method matmul of type object at 0x72f828b96ec0>(*(FakeTensor(..., size=(1, 8, 128)), FakeTensor(..., size=(1, 256, 8))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 256].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''