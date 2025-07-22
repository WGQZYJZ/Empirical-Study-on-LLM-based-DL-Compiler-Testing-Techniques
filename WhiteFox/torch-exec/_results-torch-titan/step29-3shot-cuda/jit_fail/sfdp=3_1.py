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
        self.key = torch.nn.Parameter(torch.randn(8, 32, 32, 32))

    def forward(self, x1):
        query = x1
        key = self.key
        scale_factor = torch.tensor([10000.0])
        dropout_p = 0.1
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = (v1 * scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = torch.matmul(v4, value)
        return v5



func = Model().to('cuda')



feature = 16


seq_len = 10


batch_size = 1


x1 = torch.randn(batch_size, seq_len, feature)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [256, 16] but got: [256, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x78b3a02699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 10, 16)), FakeTensor(..., device='cuda:0', size=(8, 32, 32, 32), requires_grad=True)), **{}):
Expected size for first two dimensions of batch2 tensor to be: [256, 16] but got: [256, 32].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''