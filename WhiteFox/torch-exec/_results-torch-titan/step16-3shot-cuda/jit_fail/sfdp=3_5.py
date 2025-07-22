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

    def __init__(self, hidden_size, num_segments=4, num_heads=2):
        super().__init__()
        self.dropout_p = 0.2
        self.scale_factor = np.power(hidden_size, (- 0.5))
        hidden_size_per_head = int((hidden_size / num_heads))
        self.q_key_value = torch.nn.Linear(hidden_size, ((((2 * num_segments) + 7) * num_heads) * hidden_size_per_head), bias=False)
        self.dropout = torch.nn.Dropout(p=0.2)

    def forward(self, query, key, value):
        q_key_value = self.q_key_value(query)
        q_key_value = q_key_value.reshape(q_key_value.shape[0], q_key_value.shape[1], (num_segments + 3), num_heads, hidden_size_per_head)
        q_key_value = q_key_value.permute(0, 2, 1, 3, 4)
        q = q_key_value[:, 0, :, :, :]
        k = q_key_value[:, 1, :, :, :]
        v = q_key_value[:, 2, :, :, :]
        q = q.reshape((- 1), q.shape[(- 2)], q.shape[(- 1)])
        k = k.reshape((- 1), k.shape[(- 2)], k.shape[(- 1)])
        scaled_qk = (torch.matmul(q, k.transpose((- 2), (- 1))) * self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v.reshape((- 1), v.shape[(- 2)], v.shape[(- 1)])).reshape(dropout_qk.shape[0], dropout_qk.shape[1], num_segments, num_heads, hidden_size_per_head).transpose(1, 2)
        output = output.reshape(output.shape[0], output.shape[1], (num_heads * hidden_size_per_head))
        return output



hidden_size = 1

func = Model(hidden_size).to('cuda')



query = torch.randn(1, 2, 4)



key = torch.randn(1, 10, 4)



value = torch.randn(1, 10, 4)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x4 and 1x0)

jit:
Failed running call_module L__self___q_key_value(*(FakeTensor(..., device='cuda:0', size=(1, 2, 4)),), **{}):
a and b must have same reduction dim, but got [2, 4] X [1, 0].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''