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
        super(Model, self).__init__()
        self.dropout_p = 0.1

    def forward(self, x1, x2, x3):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = ((v1 * 1.0) / math.sqrt(x2.shape[(- 1)]))
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=self.dropout_p)
        v5 = torch.matmul(v4, x3)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 100, 80)



x2 = torch.randn(1, 80, 60)



x3 = torch.randn(1, 60, 60)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 80] but got: [1, 60].

jit:
Failed running call_function <built-in method matmul of type object at 0x770b5e4699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 100, 80)), FakeTensor(..., device='cuda:0', size=(1, 60, 80))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 80] but got: [1, 60].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''