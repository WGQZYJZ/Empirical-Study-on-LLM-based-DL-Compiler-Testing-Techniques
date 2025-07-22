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

    def forward(self, query, key, value, scale_factor):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = v1.div(scale_factor)
        v3 = torch.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = torch.matmul(v4, value)
        return v5



func = Model().to('cuda')



query = torch.randn(1, 768, 196)



key = torch.randn(1, 768, 512)



value = torch.randn(1, 768, 512)



scale_factor = torch.randn(1)


test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 196] but got: [1, 512].

jit:
Failed running call_function <built-in method matmul of type object at 0x76eec48699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 768, 196)), FakeTensor(..., device='cuda:0', size=(1, 512, 768))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 196] but got: [1, 512].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''