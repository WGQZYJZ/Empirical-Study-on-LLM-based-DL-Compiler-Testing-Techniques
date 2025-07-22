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

    def forward(self, query_tensor, key_tensor, value_tensor, dropout_p=0.5, inv_scale_factor=(1.0 / math.sqrt(8))):
        qk = torch.matmul(query_tensor, key_tensor.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value_tensor)
        return output



func = Model().to('cuda')



query = torch.randn(1, 3, 64, 64)



key = torch.randn(1, 3, 64, 64)

query_tensor = 1
key_tensor = 1
value_tensor = 1

test_inputs = [query, key, query_tensor, key_tensor, value_tensor]

# JIT_FAIL
'''
direct:
matmul(): argument 'other' (position 1) must be Tensor, not int

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), 1), **{}):
matmul(): argument 'other' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''