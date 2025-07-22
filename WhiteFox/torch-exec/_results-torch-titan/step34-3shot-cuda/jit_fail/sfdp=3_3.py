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
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, q, k, v, scale_factor=1):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = (qk * scale_factor).softmax(dim=(- 1))
        dropout_qk = self.dropout(scaled_qk)
        output = self.dropout(scaled_qk).matmul(v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 10, 20)



k = torch.randn(1, 15, 25)



v = torch.randn(1, 30, 25)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 20] but got: [1, 25].

jit:
Failed running call_function <built-in method matmul of type object at 0x72c8710699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 10, 20)), FakeTensor(..., device='cuda:0', size=(1, 25, 15))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 20] but got: [1, 25].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''