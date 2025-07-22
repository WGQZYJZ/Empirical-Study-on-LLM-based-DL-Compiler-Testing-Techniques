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
        self.proj = torch.nn.Linear(3, 4)

    def forward(self, q, k, v):
        q = self.proj(q)
        k = self.proj(k)
        v = self.proj(v)
        q *= 0.5
        k *= 0.5
        dot_product = torch.matmul(q, k.transpose((- 2), (- 1)))
        attn_mask = dot_product.new_ones(dot_product.shape)
        for i in range(23):
            attn_mask[:, :, i, i] = float('-inf')
        return torch.matmul(torch.softmax((dot_product + attn_mask), dim=(- 1)), v)



func = Model().to('cuda')



q = torch.randn(1, 1, 3)



k = torch.randn(1, 2, 3)



v = torch.randn(1, 2, 3)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
too many indices for tensor of dimension 3

jit:
backend='inductor' raised:
RuntimeError: ShapeProp error for: node=%setitem : [num_users=0] = call_function[target=operator.setitem](args = (%new_ones, (slice(None, None, None), slice(None, None, None), 0, 0), -inf), kwargs = {}) with meta={'creation_timestamp': 17, 'source_fn': ('setitem', <built-in function setitem>), 'stack_trace': '  File "<string>", line 30, in forward\n'}

While executing %setitem : [num_users=0] = call_function[target=operator.setitem](args = (%new_ones, (slice(None, None, None), slice(None, None, None), 0, 0), -inf), kwargs = {})
Original traceback:
  File "<string>", line 30, in forward



You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''