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

    def __init__(self, attn_mask):
        super().__init__()
        self.attn_mask = attn_mask

    def forward(self, query, key, value):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + self.attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ value)
        return output




attn_mask = torch.arange(8).view(8, 1, 1, 1).expand(8, (- 1), 64, 64)

func = Model(attn_mask).to('cuda')



attn_mask = torch.arange(8).view(8, 1, 1, 1).expand(8, (- 1), 64, 64)



query = torch.randn(8, 2, 64, 64)



key = torch.randn(8, 2, 64, 64)



value = torch.randn(8, 2, 64, 64)


test_inputs = [attn_mask, query, key, value]

# JIT_FAIL
'''
direct:
forward() takes 4 positional arguments but 5 were given

jit:
forward() takes 4 positional arguments but 5 were given
'''