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
        self.dropout_p = 1.0
        self.dropout = torch.nn.Dropout(self.dropout_p)

    def forward(self, x1, x2, x3):
        v1 = torch.matmul(x1, torch.transpose(x2, (- 2), (- 1)))
        v2 = v1.div(0.01)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = self.dropout(v3)
        v5 = torch.matmul(v4, x3)
        return v5



func = Model().to('cuda')



x1 = torch.randn(2, 5, 3)



x2 = torch.randn(2, 3, 6)



x3 = torch.randn(2, 6, 8)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 3] but got: [2, 6].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d74db0699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 5, 3)), FakeTensor(..., device='cuda:0', size=(2, 6, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 3] but got: [2, 6].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''