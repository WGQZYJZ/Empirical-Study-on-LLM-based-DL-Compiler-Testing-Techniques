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

    def __init__(self, scaling_factor, dropout):
        super().__init__()
        self.scaling_factor = scaling_factor
        self.dropout = dropout

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.mul(self.scaling_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout)
        output = dropout_qk.matmul(x2)
        return output


scaling_factor = 1
dropout = 1
func = Model(0.6, 0.8).to('cpu')


x1 = torch.randn(1, 32, 4, 4)

x2 = torch.randn(1, 32, 10, 10)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [32, 4] but got: [32, 10].

jit:
Failed running call_function <built-in method matmul of type object at 0x7c1ba6796ec0>(*(FakeTensor(..., size=(1, 32, 4, 4)), FakeTensor(..., size=(1, 32, 10, 10))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [32, 4] but got: [32, 10].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''