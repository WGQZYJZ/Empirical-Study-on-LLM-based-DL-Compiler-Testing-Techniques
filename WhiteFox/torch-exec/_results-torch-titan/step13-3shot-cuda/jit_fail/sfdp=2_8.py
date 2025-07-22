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

    def forward(self, input_ids, attention_mask, p, inv_scale_factor, value, hidden, cell):
        q = hidden.transpose(0, 1).matmul(value)
        q = q.div(inv_scale_factor)
        att = q.softmax(dim=(- 1))
        att = torch.nn.functional.dropout(att, p=p)
        output = (att * hidden.transpose(0, 1))
        return output



func = Model().to('cuda')



input_ids = torch.LongTensor([[1, 2, 3, 4]])



attention_mask = torch.LongTensor([[1, 1, 1, 1]])



value = torch.randn(4, 128)



hidden = torch.randn(1, 4, 128)



cell = torch.randn(1, 4, 128)

p = 1
inv_scale_factor = 1

test_inputs = [input_ids, attention_mask, value, hidden, cell, p, inv_scale_factor]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''