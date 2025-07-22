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

    def forward(query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weights = torch.softmax(qk, dim=(- 1))
        output = (attn_weights @ value)
        return output



func = Model().to('cuda')



query = torch.rand(4, 1, 6)



key = torch.rand(4, 6, 2)



value = torch.rand(4, 6, 3)




attn_mask = torch.triu(torch.ones(12, 12), 1).bool()


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
forward() takes 4 positional arguments but 5 were given

jit:
forward() takes 4 positional arguments but 5 were given
'''