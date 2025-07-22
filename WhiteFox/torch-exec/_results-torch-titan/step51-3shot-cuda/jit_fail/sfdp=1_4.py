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

    def __init__(self, dim, drop_rate):
        super().__init__()
        self.dropout_p = drop_rate
        self.inv_scale_factor = (dim ** (- 0.5))

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        output = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p).matmul(value)
        return output



dim = 1
drop_rate = 1
func = Model(128, 0.1).to('cuda')



query = torch.randn(1, 128, 15)



key = torch.randn(1, 128, 20)



value = torch.randn(1, 128, 20)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 15] but got: [1, 20].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d74db0699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 128, 15)), FakeTensor(..., device='cuda:0', size=(1, 20, 128))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 15] but got: [1, 20].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''