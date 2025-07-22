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
        self.dropout = 0.1
        self.heads = 32
        self.seq_len = 256
        self.dim = 64 // self.heads

    def forward(self, input, attn_mask):
        input = torch.dropout(input, 0.2, True)
        q = input / math.sqrt(input.size(-1)) @ key.transpose(-2, -1)
        qk = q + attn_mask
        attn_weight = torch.dropout(torch.softmax(qk, dim=-1), self.dropout, True)
        output = attn_weight @ value
        return output



func = Model().to('cpu')


input = torch.randn(1, 64, 256, 64)

attn_mask = torch.randn(1, 1, 256, 256)

key = torch.randn(1, 32, 256, 64)

test_inputs = [input, attn_mask, key]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''