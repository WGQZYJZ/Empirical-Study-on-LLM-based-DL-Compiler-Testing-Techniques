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

    def __init__(self, query_size):
        super(Model, self).__init__()
        self.query_size = query_size

    def forward(self, query, key, value, mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk_float = qk.float()
        if (mask is not None):
            qk_float = qk_float.masked_fill(mask.unsqueeze(1).unsqueeze(1), float('-inf'))
        attn_weight = torch.softmax(qk_float, dim=(- 1))
        output = (attn_weight @ value)
        return output



query_size = 1
func = Model(200).to('cuda')



query = torch.randn(1, 5, 200)



key = torch.randn(1, 7, 200)



value = torch.randn(1, 7, 12)

mask = 1

test_inputs = [query, key, value, mask]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'unsqueeze'

jit:
'int' object has no attribute 'unsqueeze'

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''