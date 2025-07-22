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

    def __init__(self, n_heads=1):
        super().__init__()
        self.dropout_p = 0.5

    def forward(self, x1, x2):
        m = torch.matmul(x1, x2)
        inv_scale_factor = (m.shape[(- 1)] ** (- 0.25))
        softmax_m = m.softmax(dim=(- 1))
        dropout_m = torch.nn.functional.dropout(softmax_m, p=self.dropout_p)
        output = dropout_m.matmul(x2)
        return output




func = Model().to('cuda')



x1 = torch.randn(1, 5, 6)



x2 = torch.randn(1, 6, 7)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 7] but got: [1, 6].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 5, 7)), FakeTensor(..., device='cuda:0', size=(1, 6, 7))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 7] but got: [1, 6].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''