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
        self.dropout = torch.nn.Dropout(p=0.1)

    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(10)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        return dropout_qk.matmul(x3)



func = Model().to('cuda')



x1 = torch.randn(4, 4)



x2 = torch.randn(4, 4, 512)



x3 = torch.randn(512, 8)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 4] but got: [4, 512].

jit:
Failed running call_function <built-in method matmul of type object at 0x790e2a8699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 512, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 4] but got: [4, 512].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''