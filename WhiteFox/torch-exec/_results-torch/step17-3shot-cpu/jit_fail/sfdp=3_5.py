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

    def forward(self, query_input, key_input, value_input, query_mask, key_mask, scale_factor, dropout):
        qk = torch.matmul(query_input, key_input.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk * key_mask, p=dropout)
        output = torch.matmul(dropout_qk, value_input)
        return output


func = Model().to('cpu')


batch_size = 1
scale_factor = torch.randn(batch_size, 1, 1)
query_input = 1
key_input = 1
value_input = 1
query_mask = 1
key_mask = 1
dropout = 1

test_inputs = [scale_factor, query_input, key_input, value_input, query_mask, key_mask, dropout]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
AttributeError: 'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''