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

    def forward(self, input_tensor, scaled_factor, dropout_p):
        intermediate = input_tensor.matmul(scaled_factor.transpose(-2, -1))
        intermediate = intermediate.div(inv_scale_factor)
        softMaxIntermediate = torch.nn.functional.softmax(intermediate, dim=-1)
        dropoutIntermediate = torch.nn.functional.dropout(softMaxIntermediate, p=dropout_p)
        return dropoutIntermediate.matmul(input_tensor)


func = Model().to('cpu')


input_tensor = torch.randn(3, 5, 6)

scaled_factor = torch.randn(7, 5, 3)
dropout_p = 1

test_inputs = [input_tensor, scaled_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (7) at non-singleton dimension 0

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(3, 5, 6)), FakeTensor(..., size=(7, 3, 5))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''