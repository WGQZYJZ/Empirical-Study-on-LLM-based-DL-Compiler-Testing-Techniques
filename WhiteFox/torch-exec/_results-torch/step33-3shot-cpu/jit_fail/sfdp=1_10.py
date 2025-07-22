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
        self.query = torch.randint(low=-3, high=4, size=(2, 20, 200))
        self.key = torch.randint(low=-3, high=4, size=(10, 20, 100))
        self.value = torch.randint(low=-3, high=4, size=(10, 20, 150))

    def forward(self, query, key, value):
        v0 = torch.matmul(query, key.transpose(-2, -1))
        inv_scale_factor = pow(query.shape[-1], -0.25)
        v1 = v0.div(inv_scale_factor)
        v2 = v1.softmax(dim=-1)
        v3 = torch.nn.functional.dropout(v2, p=0.6)
        output = v3.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 20, 200)

key = torch.randn(10, 20, 100)

value = torch.randn(10, 20, 150)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [10, 200] but got: [10, 100].

jit:
Failed running call_function <built-in method matmul of type object at 0x714b07796ec0>(*(FakeTensor(..., size=(1, 20, 200)), FakeTensor(..., size=(10, 100, 20))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [10, 200] but got: [10, 100].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''