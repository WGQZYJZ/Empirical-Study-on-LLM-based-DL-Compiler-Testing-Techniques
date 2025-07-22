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

    def __init__(self, batch_size, sequence_length, embedding_size, head_num):
        super().__init__()
        self._batch_size = batch_size
        self._sequence_length = sequence_length
        self._embedding_size = embedding_size
        self.query = torch.nn.Parameter(torch.randn(batch_size, head_num, embedding_size))
        self.key = torch.nn.Parameter(torch.randn(batch_size, head_num, embedding_size))
        self.value = torch.nn.Parameter(torch.randn(batch_size, head_num, embedding_size))

    def forward(self, input, dropout_p):
        batch_size = self._batch_size
        sequence_length = self._sequence_length
        embedding_size = self._embedding_size
        head_num = self.query.size(1)
        q = self.query.permute(1, 0, 2)
        k = self.key.permute(1, 0, 2)
        v = self.value.permute(1, 0, 2)
        qk = torch.matmul(q, k.transpose(-2, -1))
        inv_scale_factor = math.sqrt(head_num * 1.0)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        output = output.permute(1, 0, 2)
        output = output.reshape((batch_size, sequence_length, embedding_size))
        return (output, dropout_qk)


batch_size = 1
sequence_length = 1
embedding_size = 1
head_num = 1
func = Model(16, 32, 64, 8).to('cpu')


input = torch.randn(16, 32, 64)
dropout_p = 1

test_inputs = [input, dropout_p]

# JIT_FAIL
'''
direct:
shape '[16, 32, 64]' is invalid for input of size 8192

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(16, 8, 64)), (16, 32, 64)), **{}):
shape '[16, 32, 64]' is invalid for input of size 8192

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''