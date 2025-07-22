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
        self.scale_factor = nn.Parameter(torch.ones(1, 1, 1))

    def forward(self, attention_mask, att_output):
        attention_mask = attention_mask.softmax(dim=(- 1))
        attention_mask = torch.nn.functional.dropout(attention_mask, p=dropout_p)
        output = attention_mask.matmul(att_output)
        return output



func = Model().to('cuda')



att_output = torch.randn(1, 1, 100, 5)

attention_mask = 1

test_inputs = [att_output, attention_mask]

# JIT_FAIL
'''
direct:
matmul(): argument 'other' (position 1) must be Tensor, not int

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 1, 100, 5)), 1), **{}):
matmul(): argument 'other' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''