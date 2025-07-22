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
        self.drop = torch.nn.Dropout(0.1)

    def forward(self, q, k, v):
        qk = torch.matmul(query, key.transpose(-2, -1))
        inv_scale_factor = 0.125
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.drop(softmax_qk)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 128, 512)

key = torch.randn(1, 128, 512)
q = 1

test_inputs = [query, key, q]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 3].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(1, 128, 128)), FakeTensor(..., size=(1, 3, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 3].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''