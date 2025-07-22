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

    def __init__(self, input_shape):
        super().__init__()
        self.hidden_dims = (((input_shape[0] * input_shape[1]) * input_shape[2]), ((8 * input_shape[2]) * input_shape[3]))
        self.query = torch.nn.Linear(*self.hidden_dims)
        self.key = torch.nn.Linear(*self.hidden_dims)
        self.value = torch.nn.Linear(*self.hidden_dims)

    def forward(self, x1):
        qk = self.query(x1).matmul(self.key(x1).transpose((- 2), (- 1)))
        in_scale_factor = np.sqrt(q.size((- 1)))
        softmax_qk = (qk / in_scale_factor).softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, training=True)
        self.dropout_qk = dropout_qk
        output = self.dropout_qk.matmul(self.value(x1))
        return output



input_shape = 1
func = Model((3, 16, 64, 64)).to('cuda')



x1 = torch.randn(3, 16, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3072x64 and 3072x32768)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(3, 16, 64, 64)),), **{}):
a and b must have same reduction dim, but got [3072, 64] X [3072, 32768].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''