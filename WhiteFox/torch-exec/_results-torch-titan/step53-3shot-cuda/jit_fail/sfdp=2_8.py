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

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = v1.div(inv_scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=dropout_p, train=self.training)
        output = v4.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(200, 512)



key = torch.randn(200, 512, 16)



value = torch.randn(200, 512, 16)



inv_scale_factor = torch.randn(200, 512, 16)

dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [200, 512] but got: [200, 16].

jit:
Failed running call_function <built-in method matmul of type object at 0x79536ac699e0>(*(FakeTensor(..., device='cuda:0', size=(200, 512)), FakeTensor(..., device='cuda:0', size=(200, 16, 512))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [200, 512] but got: [200, 16].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''