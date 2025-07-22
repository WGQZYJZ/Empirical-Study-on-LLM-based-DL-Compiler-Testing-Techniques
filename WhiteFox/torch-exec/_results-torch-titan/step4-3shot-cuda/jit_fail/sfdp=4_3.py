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

    def forward(self, query, key, value, masking=None):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        attn_mask = (0 * qk)
        if masking:
            attn_mask = ((- 1e+20) * torch.ones_like(qk))
            for i in masking:
                attn_mask[:, i:(i + 1), :] = 0
                attn_mask[:, :, i:(i + 1)] = 0
        qk = (qk / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        return torch.matmul(attn_weight, value)



func = Model().to('cuda')



query = torch.randn(1, 8, 10)



key = torch.randn(1, 4, 12)



value = torch.randn(1, 4, 16)



pe = torch.zeros(20, 768)



position = torch.arange(0, 20).unsqueeze(1)


test_inputs = [query, key, value, pe, position]

# JIT_FAIL
'''
direct:
forward() takes from 4 to 5 positional arguments but 6 were given

jit:
forward() takes from 4 to 5 positional arguments but 6 were given
'''