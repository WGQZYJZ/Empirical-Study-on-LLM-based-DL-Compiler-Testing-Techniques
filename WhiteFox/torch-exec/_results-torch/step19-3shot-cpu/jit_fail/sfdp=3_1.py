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
        self.scale_factor = torch.nn.Parameter(torch.tensor(0.5))

    def forward(self, value, query, key, dropout_p):
        softmax_qk = torch.nn.functional.softmax(query @ key.transpose(-2, -1), dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk @ value


func = Model().to('cpu')


value = torch.randn(1, 2, 3)

query = torch.randn(1, 3, 4)

key = torch.randn(1, 4, 2)


dropout_p = torch.nn.Parameter(torch.tensor(0.7))

test_inputs = [value, query, key, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 4] but got: [1, 2].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(1, 3, 4)), FakeTensor(..., size=(1, 2, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 4] but got: [1, 2].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''