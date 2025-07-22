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

    def __init__(self, model_config):
        super().__init__()
        self.model_config = model_config

    def forward(self, q, k, v, m, m_mask):
        qk = (torch.matmul(q, k.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1))))
        scaled_qk = qk.div(self.model_config.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.model_config.dropout_p)
        output = dropout_qk.matmul(v)
        return output



model_config = 1

func = Model(model_config).to('cuda')



q = torch.randn(1, 64, 64)



k = torch.randn(1, 64, 64)



v = torch.randn(1, 64, 64)



m_mask = torch.ones(1, 64, 6, device='cpu')

m = 1

test_inputs = [q, k, v, m_mask, m]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'scale_factor'

jit:
'int' object has no attribute 'scale_factor'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''