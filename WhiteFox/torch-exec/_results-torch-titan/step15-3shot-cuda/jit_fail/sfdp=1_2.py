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

    def __init__(self, num_heads, num_qk, dropout_p):
        super().__init__()
        self.num_heads = num_heads
        self.num_qk = num_qk
        self.W_query = torch.nn.Parameter(torch.FloatTensor(num_heads, num_qk, 32))
        self.W_key = torch.nn.Parameter(torch.FloatTensor(num_heads, num_qk, 32))
        self.W_value = torch.nn.Parameter(torch.FloatTensor(num_heads, num_qk, 32))
        self.dropout_p = dropout_p
        self.scaled_qk = None

    def forward(self, x1, x2):
        qb = torch.bmm(x1, self.W_query)
        kb = torch.bmm(x2, self.W_key)
        self.scaled_qk = torch.bmm(qb.transpose(1, 2), kb)
        num_units = (self.num_heads * self.num_qk)
        scaled_qk = self.scaled_qk
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(self.W_value.reshape(num_units, (- 1)).transpose(1, 0).unsqueeze(0))
        output = output.reshape(x1.shape[0], (- 1), output.shape[(- 1)]).transpose(1, 2)
        return output



num_heads = 1
num_qk = 1
dropout_p = 1

func = Model(num_heads, num_qk, dropout_p).to('cuda')



x1 = torch.randn(1, 32, 64)



x2 = torch.randn(1, 32, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 64] but got: [1, 1].

jit:
Failed running call_function <built-in method bmm of type object at 0x7338538699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 1, 32), requires_grad=True))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 64] but got: [1, 1].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''