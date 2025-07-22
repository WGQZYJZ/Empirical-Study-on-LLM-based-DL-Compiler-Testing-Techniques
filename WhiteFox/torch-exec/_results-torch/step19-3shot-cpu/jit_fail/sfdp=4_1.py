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

    def __init__(self, query_num, key_num, value_num):
        super().__init__()

    def forward(self, q, k, v, attn_mask):
        qk = np.matmul(q, k.transpose(1, 0, 2))
        qk = qk / math.sqrt(k.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = torch.matmul(attn_weight, v)
        return output


query_num = 1
key_num = 1
value_num = 1

func = Model(query_num, key_num, value_num).to('cpu')

q = 1
k = 1
v = 1
attn_mask = 1

test_inputs = [q, k, v, attn_mask]

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