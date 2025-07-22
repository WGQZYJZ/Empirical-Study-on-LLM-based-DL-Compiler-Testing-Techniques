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

    def __init__(self, dropout_p: float):
        super().__init__()
        self.dropout_p = dropout_p
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(self.dropout_p)

    def forward(self, x1, x2):
        v1 = x1.matmul(x2.transpose((- 2), (- 1)))
        scale_factor = math.sqrt(x2.size((- 1)))
        inv_scale_factor = (1.0 / scale_factor)
        v2 = v1.div(inv_scale_factor)
        v3 = self.softmax(v2)
        v4 = self.dropout(v3)
        v5 = v4.matmul(x2)
        return v5



dropout_p = 1
func = Model(0.2).to('cuda')



x1 = torch.randn(1, 32, 6)



x2 = torch.randn(1, 6, 4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 6] but got: [1, 4].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 32, 6)), FakeTensor(..., device='cuda:0', size=(1, 4, 6))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 6] but got: [1, 4].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''