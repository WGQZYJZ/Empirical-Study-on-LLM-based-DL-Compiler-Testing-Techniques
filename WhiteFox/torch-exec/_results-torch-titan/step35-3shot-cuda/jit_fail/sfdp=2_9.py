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

    def __init__(self, hidden_size, dropout_p):
        super().__init__()
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p
        self.fc_q = torch.nn.Linear(hidden_size, hidden_size)
        self.fc_k = torch.nn.Linear(hidden_size, hidden_size)
        self.fc_v = torch.nn.Linear(hidden_size, hidden_size)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        v = torch.nn.functional.dropout(value, self.dropout_p)
        scaled_qk = qk.div(v.size((- 1)))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        v = torch.nn.functional.dropout(v.transpose((- 2), (- 1)).softmax(dim=(- 1)).transpose((- 2), (- 1)), self.dropout_p)
        return torch.matmul(softmax_qk, v)

    def gen_sample(self, batch_size):
        return (torch.randint(0, self.hidden_size, size=(batch_size, 3, self.hidden_size)), torch.randn(batch_size, 3, self.hidden_size))



hidden_size = 1
dropout_p = 1
func = Model(512, 0.1).to('cuda')

query = 1
key = 1
value = 1

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''