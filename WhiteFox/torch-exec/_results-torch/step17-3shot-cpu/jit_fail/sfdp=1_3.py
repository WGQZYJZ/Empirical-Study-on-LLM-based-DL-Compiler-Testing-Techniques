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

    def __init__(self, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.dropout_p = 0.1
        self.head_dim = 32
        self.output_dim = self.num_heads * self.head_dim

    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        inv_scale_factor = 1.0 / np.sqrt(self.head_dim)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(x3)
        return output


num_heads = 1

func = Model(num_heads).to('cpu')


x1 = torch.randn(12, 48, 32)

x2 = torch.randn(12, 32, 24)

x3 = torch.randn(12, 24, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [12, 32] but got: [12, 24].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d808b196ec0>(*(FakeTensor(..., size=(12, 48, 32)), FakeTensor(..., size=(12, 24, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [12, 32] but got: [12, 24].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''