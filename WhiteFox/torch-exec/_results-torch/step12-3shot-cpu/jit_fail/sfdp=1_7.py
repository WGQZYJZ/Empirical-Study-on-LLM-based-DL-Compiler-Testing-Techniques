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

    def forward(self, __input_query__, __input_key__, __input_value__, __input_dropout_p__, __input_inv_scale_factor__):
        __compute_the_dot_product__ = torch.matmul(__input_query__, __input_key__.transpose(-2, -1))
        __scaled_qk = __compute_the_dot_product__.div(__input_inv_scale_factor__)
        __softmax_qk = scaled_qk.softmax(dim=-1)
        __dropout_qk = torch.nn.functional.dropout(__softmax_qk, p=__input_dropout_p__)
        __compute_the_dot_product__ = __dropout_qk.matmul(__input_value__)
        return __compute_the_dot_product__


func = Model().to('cpu')


__input_query__ = torch.randn(16, 32, 16)

__input_key__ = torch.randn(8, 64, 8)

__input_value__ = torch.randn(8, 64, 8)

__input_dropout_p__ = torch.tensor(0.01)

__input_inv_scale_factor__ = torch.tensor(1.0)

test_inputs = [__input_query__, __input_key__, __input_value__, __input_dropout_p__, __input_inv_scale_factor__]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (8) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x779db0b96ec0>(*(FakeTensor(..., size=(16, 32, 16)), FakeTensor(..., size=(8, 8, 64))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''