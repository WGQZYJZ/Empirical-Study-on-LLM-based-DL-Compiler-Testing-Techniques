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

    def forward(self, queries, keys, values, dropout=0.5, scale_factor=None, mask=None):
        qk = torch.matmul(queries, keys.transpose((- 2), (- 1)))
        if (scale_factor is not None):
            inv_scale_factor = (1 / scale_factor)
            scaled_qk = qk.div(inv_scale_factor)
        else:
            scaled_qk = qk
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout)
        output = dropout_qk.matmul(values)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 3, 128, 256)



x2 = torch.randn(1, 3, 256, 128)



x3 = torch.randn(1, 3, 256, 512)

queries = 1
keys = 1
values = 1

test_inputs = [x1, x2, x3, queries, keys, values]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 256] but got: [3, 128].

jit:
Failed running call_function <built-in method matmul of type object at 0x76a0a1a699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 128, 256)), FakeTensor(..., device='cuda:0', size=(1, 3, 128, 256))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 256] but got: [3, 128].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''