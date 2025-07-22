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

    def forward(self, q, k):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(2)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


q1 = torch.randn(1, 5, 2)

k1 = torch.randn(1, 3, 6)

test_inputs = [q1, k1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 6].

jit:
Failed running call_function <built-in method matmul of type object at 0x7fbc79d96ec0>(*(FakeTensor(..., size=(1, s2, s3)), FakeTensor(..., size=(1, s1, s0))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, s3] but got: [1, s1].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''