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

    def __init__(self, query_size=20, key_size=12, value_size=5, head_num=2, dropout_p=0.0):
        super().__init__()
        self.dropout_p = dropout_p
        self.head_num = head_num
        self.dropout_qk = torch.nn.Dropout(self.dropout_p)
        self.matmul_qk = torch.nn.Linear((query_size + key_size), head_num)

    def forward(self, query, key, value, inv_scale_factor):
        batch_size = query.shape[0]
        qk = self.matmul_qk(torch.cat([query, key], dim=(- 1)))
        qk = qk.reshape(batch_size, (- 1), self.head_num).transpose(dim0=(- 2), dim1=(- 1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout_qk(softmax_qk)
        output = dropout_qk.matmul(value.reshape(batch_size, (- 1), self.head_num).transpose(dim0=(- 2), dim1=(- 1)))
        return output.reshape(batch_size, (- 1))



func = Model().to('cuda')



query = torch.randn(8, 20, 64)



key = torch.randn(8, 12, 64)



value = torch.randn(8, 5, 64)



inv_scale_factor = torch.randn(1)


test_inputs = [query, key, value, inv_scale_factor]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 2. Expected size 20 but got size 12 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x72566de699e0>(*([FakeTensor(..., device='cuda:0', size=(8, 20, 64)), FakeTensor(..., device='cuda:0', size=(8, 12, 64))],), **{'dim': -1}):
Sizes of tensors must match except in dimension 2. Expected 20 but got 12 for tensor number 1 in the list

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''