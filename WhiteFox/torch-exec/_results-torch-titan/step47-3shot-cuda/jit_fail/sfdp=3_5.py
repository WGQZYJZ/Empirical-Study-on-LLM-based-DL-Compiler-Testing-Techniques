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
        self.emb = torch.nn.Embedding(10, 32)
        self.proj = torch.nn.Linear(self.emb.embedding_dim, 16)
        self.scale_factor = 4.5

    def forward(self, q, k):
        v_emb = self.emb(v)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = torch.softmax(scaled_qk, dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v_emb)
        return output



func = Model().to('cuda')



q = torch.randn(2, 64, 32)



k = torch.randn(8, 138, 32)


test_inputs = [q, k]

# JIT_FAIL
'''
direct:
Expected tensor for argument #1 'indices' to have one of the following scalar types: Long, Int; but got torch.FloatTensor instead (while checking arguments for embedding)

jit:
Failed running call_module L__self___emb(*(FakeTensor(..., size=(2, 5, 2, 8)),), **{}):
tensors used as indices must be long, int, byte or bool tensors

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''