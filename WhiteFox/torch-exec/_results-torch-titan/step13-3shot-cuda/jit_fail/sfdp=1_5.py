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

    def scaled_dot_product_attention(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

    def cross_attend(self, query, key, value, inv_scale_factor=1.0, dropout_p=0.0):
        cross_attend_qk = self.scaled_dot_product_attention(query, key, value, inv_scale_factor, dropout_p)
        cross_attend_v = self.scaled_dot_product_attention(value, value, value, inv_scale_factor, dropout_p)
        return (cross_attend_qk, cross_attend_v)

    def forward(self, x1, x2, x3):
        x1 = x1.permute([0, 2, 1])
        x2 = x2.permute([1, 2, 0])
        x3 = x3.permute([0, 2, 1])
        (v1, v2) = self.cross_attend(x1, x2, x1, inv_scale_factor=0.2, dropout_p=0.2)
        v3 = self.scaled_dot_product_attention(v1, x3, v2, inv_scale_factor=0.2, dropout_p=0.2)
        v4 = v3.permute([2, 1, 0])
        return v4



func = Model().to('cuda')



x1 = torch.randn(8, 4, 32)



x2 = torch.randn(32, 4, 8)



x3 = torch.randn(8, 32, 8)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (4) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x7a75daa699e0>(*(FakeTensor(..., device='cuda:0', size=(8, 32, 4)), FakeTensor(..., device='cuda:0', size=(4, 32, 8))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 37, in forward
  File "<string>", line 29, in cross_attend
  File "<string>", line 21, in scaled_dot_product_attention


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''