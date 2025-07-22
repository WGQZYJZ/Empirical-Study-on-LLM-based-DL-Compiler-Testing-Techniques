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
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.matmul1 = torch.nn.Linear(5, 4)
        self.matmul2 = torch.nn.Linear(4, 3)
        self.matmul3 = torch.nn.Linear(4, 2)

    def forward(self, q, k, v, inv_scale_factor, dropout_p):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v1 = self.matmul1(dropout_qk)
        v2 = torch.transpose(v1, (- 2), (- 1))
        v3 = self.matmul2(torch.transpose(v2, (- 1), (- 2)))
        v4 = self.matmul3(v3)
        output = torch.transpose(v4, (- 2), (- 1))
        return output



func = Model().to('cuda')



q = torch.randn(2, 4, 5)



k = torch.randn(2, 5, 3)



v = torch.randn(2, 5, 2)

inv_scale_factor = 1
dropout_p = 1

test_inputs = [q, k, v, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 3].

jit:
Failed running call_function <built-in method matmul of type object at 0x7858a60699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 4, 5)), FakeTensor(..., device='cuda:0', size=(2, 3, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 3].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''