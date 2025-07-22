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

    def forward(self, queries, keys, values, scale_factor, dropout_p):
        qk = torch.matmul(queries, keys.transpose((- 2), (- 1)))
        scaled_qk = qk.div(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, values)
        return output



func = Model().to('cuda')



queries = torch.randn(1, 2, 20)



keys = torch.randn(1, 2, 40)



values = torch.randn(1, 2, 40)



scale_factor = torch.randn(1, 1)

dropout_p = 1

test_inputs = [queries, keys, values, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 20] but got: [1, 40].

jit:
Failed running call_function <built-in method matmul of type object at 0x765a484699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 20)), FakeTensor(..., device='cuda:0', size=(1, 40, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 20] but got: [1, 40].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''