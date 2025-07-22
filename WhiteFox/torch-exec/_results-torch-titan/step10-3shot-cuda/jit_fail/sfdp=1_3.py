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
        self.attention_head_size = None
        self.hidden_size = None

    def forward(self, query, key, value, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1))).div((self.attention_head_size ** 0.5))
        softmax_qk = torch.nn.functional.softmax(qk, dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output



func = Model().to('cuda')



query = torch.randn(10, 5, 64)



key = torch.randn(10, 3, 64, 64)



value = torch.randn(10, 4, 64, 32)

dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x70dda8a699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 5, 64)), FakeTensor(..., device='cuda:0', size=(10, 3, 64, 64))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''