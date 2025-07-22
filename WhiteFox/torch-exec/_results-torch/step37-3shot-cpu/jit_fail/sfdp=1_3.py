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

    def __init__(self, config):
        super(Model, self).__init__()
        self.config = config
        self.w = torch.randn(3, 3, 1, 1)

    def forward(self, x1):
        qk = torch.matmul(x1, self.w.transpose(-2, -1))
        scaled_qk = qk.div(self.config.div)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.config.dropout)
        output = dropout_qk.matmul(x1)
        return output


config = 1

func = Model(config).to('cpu')


x1 = torch.randn(1, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [9, 3] but got: [9, 1].

jit:
Failed running call_function <built-in method matmul of type object at 0x7fbc79d96ec0>(*(FakeTensor(..., size=(1, 3)), FakeTensor(..., size=(3, 3, 1, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [9, 3] but got: [9, 1].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''