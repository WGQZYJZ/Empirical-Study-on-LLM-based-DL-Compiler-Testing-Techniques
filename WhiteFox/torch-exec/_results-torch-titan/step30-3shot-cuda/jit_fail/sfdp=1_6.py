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
        self.emb_dim = 64
        self.dropout_p = 0

    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div((self.emb_dim ** (- 0.5)))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 2, 64)



k = torch.randn(1, 4, 64)



v = torch.randn(4, 2, 64)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 4] but got: [4, 2].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 2, 4)), FakeTensor(..., device='cuda:0', size=(4, 2, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 4] but got: [4, 2].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''