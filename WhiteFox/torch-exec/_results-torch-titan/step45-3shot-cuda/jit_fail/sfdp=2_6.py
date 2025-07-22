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

    def __init__(self, d_model, nhead):
        super().__init__()
        self.d_model = d_model
        self.nhead = nhead

    def forward(self, inp_query, inp_key, inp_value, inp_key_padding_mask):
        query = inp_query.view((- 1), 1, (inp_query.size((- 1)) // self.nhead), self.nhead, self.d_model)
        key = inp_key.view((- 1), 1, (inp_key.size((- 1)) // self.nhead), self.nhead, self.d_model)
        value = inp_value.view((- 1), 1, (inp_value.size((- 1)) // self.nhead), self.nhead, self.d_model)
        key_padding_mask = inp_key_padding_mask.view((- 1), 1, 1, self.nhead)
        v1 = torch.matmul(query, key.transpose((- 2), (- 1))).div((self.d_model ** 0.5))
        v2 = v1.softmax(dim=(- 1))
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)
        v4 = v3.reshape(inp_query.size((- 2)), inp_query.size((- 1)), self.nhead, (- 1)).transpose((- 2), (- 1))
        v5 = torch.matmul(v4, value).reshape(v4.size((- 1)), self.nhead, (- 1))
        return v5



d_model = 1
nhead = 1

func = Model(d_model, nhead).to('cuda')

inp_query = 1
inp_key = 1
inp_value = 1
inp_key_padding_mask = 1

test_inputs = [inp_query, inp_key, inp_value, inp_key_padding_mask]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'view'

jit:
'int' object has no attribute 'view'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''