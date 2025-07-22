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

    def __init__(self, hidden):
        super().__init__()
        self.embedding = torch.nn.Embedding(100, hidden)

    def forward(self, k, q, v):
        d = self.embedding(k)
        e1 = torch.matmul(q, d.tranpose((- 2), (- 1)))
        e2 = (e1 * 100)
        softmax_e2 = torch.softmax(e2, dim=(- 1))
        dropout_e2 = torch.nn.functional.dropout(softmax_e2, p=0.8)
        output = torch.matmul(dropout_e2, v)
        return output



hidden = 1
func = Model(20).to('cuda')



k = torch.randint(0, 100, (1, 15)).long()



q = torch.randn(1, 17, 20)



v = torch.randn(1, 15, 20)


test_inputs = [k, q, v]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute 'tranpose'

jit:
Failed running call_method tranpose(*(FakeTensor(..., device='cuda:0', size=(1, 15, 20)), -2, -1), **{}):
'FakeTensor' object has no attribute 'tranpose'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''