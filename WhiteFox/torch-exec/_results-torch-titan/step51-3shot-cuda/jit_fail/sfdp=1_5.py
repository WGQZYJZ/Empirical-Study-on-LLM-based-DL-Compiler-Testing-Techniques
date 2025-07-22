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

    def __init__(self, num_heads=8, dropout_p=0.1, scale_factor=(128 ** (- 0.5))):
        super().__init__()
        self.scale_factor = scale_factor
        self.q = torch.nn.Linear(128, 128)
        self.k = torch.nn.Linear(128, 128)
        self.v = torch.nn.Linear(128, 128)

    def forward(self, data, mask):
        q_data = self.q(data)
        k_data = self.k(data)
        v_data = self.v(data)
        qk_data = torch.matmul(q_data, k_data.transpose((- 2), (- 1)))
        scaled_qk_data = qk_data.div(self.scale_factor)
        softmax_qk_data = scaled_qk_data.softmax(dim=(- 1))
        dropout_qk_data = torch.nn.functional.dropout(softmax_qk_data, p=dropout_p, mask=mask)
        output = torch.matmul(dropout_qk_data, v_data)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 64, 128)



mask = torch.zeros(1, 64, 64).bool()


test_inputs = [x1, mask]

# JIT_FAIL
'''
direct:
name 'dropout_p' is not defined

jit:
name 'dropout_p' is not defined

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''