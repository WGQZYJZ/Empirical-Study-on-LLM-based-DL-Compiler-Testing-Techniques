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

    def forward(self, query, key, value, inv_scale_factor, dropout_p, dropout_enabled):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        if dropout_enabled:
            dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        else:
            dropout_qk = softmax_qk
        return dropout_qk.matmul(value)



func = Model().to('cuda')



query = torch.randn(3, 256, 20)



key = torch.randn(3, 256, 256)



value = torch.randn(3, 256, 256)

inv_scale_factor = 1
dropout_p = 1
dropout_enabled = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p, dropout_enabled]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 20] but got: [3, 256].

jit:
Failed running call_function <built-in method matmul of type object at 0x7eadf9c699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 256, 20)), FakeTensor(..., device='cuda:0', size=(3, 256, 256))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 20] but got: [3, 256].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''