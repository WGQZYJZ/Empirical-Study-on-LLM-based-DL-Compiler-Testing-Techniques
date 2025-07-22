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

    def forward(query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ value)
        return output



func = Model().to('cuda')



query = torch.randn(20, 128, 50)



key = torch.randn(20, 128, 64)



value = torch.randn(20, 128, 64)



attn_mask = torch.randn((20, 1, 50, 64))


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
forward() takes 4 positional arguments but 5 were given

jit:
forward() takes 4 positional arguments but 5 were given
'''