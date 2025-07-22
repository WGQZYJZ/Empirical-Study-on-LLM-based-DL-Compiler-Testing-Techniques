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

    def forward(self, queries, keys, values):
        dot_product = torch.matmul(queries, keys.transpose((- 2), (- 1)))
        scaled_dot_prod = (dot_product / math.sqrt(query.size((- 1))))
        softmax_dot_prod = F.softmax(scaled_dot_prod, dim=(- 1))
        dropout_dot_prod = F.dropout(softmax_dot_prod, p=0.5, training=self.training)
        output = torch.matmul(dropout_dot_prod, value)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 32, 64)



x2 = torch.randn(1, 64, 32)

queries = 1

test_inputs = [x1, x2, queries]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 64] but got: [1, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x71703e2699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 64)), FakeTensor(..., device='cuda:0', size=(1, 32, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 64] but got: [1, 32].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''