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

    def __init__(self, scale_factor=(2 ** 0.5), dropout_p=0.5):
        super().__init__()
        self.dropout_p = dropout_p
        self.scale_factor = scale_factor

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 2, 256)



key = torch.randn(1, 2, 512)



value = torch.randn(1, 2, 512)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 256] but got: [1, 512].

jit:
Failed running call_function <built-in method matmul of type object at 0x72c8710699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 256)), FakeTensor(..., device='cuda:0', size=(1, 512, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 256] but got: [1, 512].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''