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

    def forward(self, input_tensor, key, value, inv_scale_factor, dropout_p):
        result_1 = torch.matmul(query, key.transpose(-2, -1))
        result_2 = result_1.div(inv_scale_factor)
        result_3 = result_2.softmax(dim=-1)
        result_4 = torch.nn.functional.dropout(result_3, p=dropout_p)
        result_5 = result_4.matmul(value)
        return result_5


func = Model().to('cpu')


query = torch.randn(2, 3, 48, 64)

key = torch.randn(2, 3, 432, 56)

value = torch.randn(2, 3, 48, 56)

inv_scale_factor = torch.zeros((2, 3, 1, 1)).fill_(10).requires_grad_()
input_tensor = 1

test_inputs = [query, key, value, inv_scale_factor, input_tensor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [6, 64] but got: [6, 56].

jit:
Failed running call_function <built-in method matmul of type object at 0x74f71e996ec0>(*(FakeTensor(..., size=(2, 3, 48, 64)), FakeTensor(..., size=(2, 3, s3, s2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [6, 64] but got: [6, s3].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''