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
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 * scale_factor
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = self.dropout(v3)
        output = torch.matmul(v4, x2)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 2, 3)

x2 = torch.randn(1, 3, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 2].

jit:
Failed running call_function <built-in method matmul of type object at 0x7ad738996ec0>(*(FakeTensor(..., size=(1, 2, 3)), FakeTensor(..., size=(1, 2, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 2].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''