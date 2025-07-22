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

    def __init__(self, dropout_p=0.2):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, query, key, value, inv_scale_factor):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 1, 1, 16)



key = torch.randn(1, 1, 16, 1)



value = torch.randn(1, 1, 1, 16)



inv_scale_factor = torch.randn(1)


test_inputs = [query, key, value, inv_scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 1].

jit:
Failed running call_function <built-in method matmul of type object at 0x72566de699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 16)), FakeTensor(..., device='cuda:0', size=(1, 1, 1, 16))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 1].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''