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
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, query, key, value, inv_scale_factor):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 5, 10)



key = torch.randn(1, 10, 5)



value = torch.randn(1, 5, 20)



inv_scale_factor = torch.randn(1)


test_inputs = [query, key, value, inv_scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 10] but got: [1, 5].

jit:
Failed running call_function <built-in method matmul of type object at 0x7df4800699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 10)), FakeTensor(..., device='cuda:0', size=(1, 5, 10))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 10] but got: [1, 5].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''