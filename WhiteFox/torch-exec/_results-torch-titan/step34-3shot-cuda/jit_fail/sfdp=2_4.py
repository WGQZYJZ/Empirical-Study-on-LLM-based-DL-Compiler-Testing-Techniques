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

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = torch.rsqrt(torch.tensor(float(qk.size((- 1)))))
        scaled_qk = torch.div(qk, inv_scale_factor)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = (dropout_qk.matmul(value),)
        return output



func = Model().to('cuda')



query = torch.randn(1, 16, 512)



key = torch.randn(1, 16, 128)



value = torch.randn(1, 16, 128)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 512] but got: [1, 128].

jit:
Failed running call_function <built-in method matmul of type object at 0x7eadf9c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 512)), FakeTensor(..., device='cuda:0', size=(1, 128, 16))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 512] but got: [1, 128].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''