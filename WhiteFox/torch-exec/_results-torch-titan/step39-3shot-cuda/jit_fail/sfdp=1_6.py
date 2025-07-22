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

    def make_query_key_value(self, m, q, k, v):
        (mk, qk, vk) = m.split((m.shape[0] // 3), dim=0)
        return (qk, mk, vk)

    def forward(self, q, k, v):
        (qk, mk, vk) = self.make_query_key_value(q, q, k, v)
        scale_factor = ((mk.shape[0] * mk.shape[(- 1)]) ** (- 0.25))
        inv_scale_factor = (1 / scale_factor)
        qk = qk.matmul(k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)
        return dropout_qk.matmul(v)



func = Model().to('cuda')



q = torch.randn(14, 20, 10)



k = torch.randn(20, 3, 80)



v = torch.randn(20, 80)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
too many values to unpack (expected 3)

jit:


from user code:
   File "<string>", line 25, in forward
  File "<string>", line 21, in make_query_key_value


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''