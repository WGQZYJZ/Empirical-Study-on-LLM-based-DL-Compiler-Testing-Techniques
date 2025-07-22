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
        self.in_dim = 12
        self.out_dim = 6
        self.dropout_p = 0.2
        self.scale_factor = (1 / math.sqrt(self.in_dim))

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.T)
        scaled_qk = (self.scale_factor * qk)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 1, 12)



key = torch.randn(1, 100, 12)



value = torch.randn(1, 100, 6)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [12, 12] but got: [12, 100].

jit:
Failed running call_function <built-in method matmul of type object at 0x7ace4a0699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 12)), FakeTensor(..., device='cuda:0', size=(12, 100, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [12, 12] but got: [12, 100].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''