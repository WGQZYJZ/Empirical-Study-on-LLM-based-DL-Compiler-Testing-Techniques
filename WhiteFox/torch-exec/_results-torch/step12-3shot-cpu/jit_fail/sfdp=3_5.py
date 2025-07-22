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

    def __init__(self, hidden_size=128, nhead=8, scaling_factor=0.2):
        super(Model, self).__init__()
        self.hidden_size = hidden_size
        self.nhead = nhead
        self.scaling_factor = scaling_factor
        self.fc_query = torch.nn.Linear(hidden_size, hidden_size)
        self.fc_key = torch.nn.Linear(hidden_size, hidden_size)
        self.fc_value = torch.nn.Linear(hidden_size, hidden_size)

    def forward(self, q, k, v, dropout_p):
        q = self.fc_query(q)
        k = self.fc_key(k)
        v = self.fc_value(v)
        q = q.view(-1, q.size(1), self.nhead, self.hidden_size // self.nhead).transpose(0, 1)
        k = k.view(-1, k.size(1), self.nhead, self.hidden_size // self.nhead).transpose(0, 1)
        v = v.view(-1, v.size(1), self.nhead, self.hidden_size // self.nhead).transpose(0, 1)
        q = q / math.sqrt(self.hidden_size)
        _sq = torch.sum(q ** 2, -1)
        _sk = torch.matmul(k.transpose(-1, -2), q) / math.sqrt(self.hidden_size)
        _s = _sq[..., None] + _sk[..., None] + (_sk.transpose(-1, -2) - _sq[..., None]).abs() * self.scaling_factor
        attn = torch.softmax(_s, dim=-1)
        if dropout_p > 0:
            attn = torch.nn.functional.dropout(attn, p=dropout_p)
        output = torch.matmul(attn, v)
        output = output.transpose(0, 1).contiguous().view(output.size()[1], -1)
        return output


func = Model().to('cpu')


q = torch.rand(3, 5, 128)

k = torch.rand(3, 6, 128)

v = torch.rand(3, 6, 128)
dropout_p = 1

test_inputs = [q, k, v, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (5) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x7665fad96ec0>(*(FakeTensor(..., size=(6, 3, 16, 8)), FakeTensor(..., size=(5, 3, 8, 16))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''