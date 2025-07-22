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

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.scale_factor = torch.tensor(1.0 / math.sqrt(768))

    def forward(self, x, y):
        qk = torch.matmul(x, y.T)
        scaled_qk = qk * self.scale_factor
        softmax_qk = softmax(scaled_qk.transpose(-2, -1)).transpose(-2, -1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5, training=self.training)
        output = torch.matmul(dropout_qk, y)
        return output


func = Model().to('cpu')


x = torch.randn(64, 768)

y = torch.randn(768, 2048)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x768 and 2048x768)

jit:
Failed running call_function <built-in method matmul of type object at 0x7665fad96ec0>(*(FakeTensor(..., size=(64, 768)), FakeTensor(..., size=(2048, 768))), **{}):
a and b must have same reduction dim, but got [64, 768] X [2048, 768].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''