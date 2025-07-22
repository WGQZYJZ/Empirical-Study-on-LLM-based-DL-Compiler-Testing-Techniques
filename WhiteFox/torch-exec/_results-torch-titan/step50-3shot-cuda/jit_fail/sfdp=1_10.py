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
        self.embed_dim = 128
        self.num_heads = 12

    def forward(self, q, k, v):
        inv_scale_factor = ((self.embed_dim // self.num_heads) ** (- 0.5))
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.4)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(16, 16, 128)



key = torch.randn(16, 16, 128)

q = 1

test_inputs = [query, key, q]

# JIT_FAIL
'''
direct:
name 'value' is not defined

jit:
name 'value' is not defined

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''