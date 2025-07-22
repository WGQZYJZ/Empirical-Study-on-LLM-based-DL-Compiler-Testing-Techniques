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

    def __init__(self, d_model, nhead, dim_feedforward):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(d_model, nhead)

    def forward(self, src, src_mask=None):
        (output, _) = self.attention(src, src, src, src_mask=src_mask)
        return output


d_model = 1
nhead = 1
dim_feedforward = 1

func = Model(d_model, nhead, dim_feedforward).to('cpu')


src = torch.randn(4, 32, 128)

src_mask = torch.randn(4, 4)

test_inputs = [src, src_mask]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'src_mask'

jit:
forward() got an unexpected keyword argument 'src_mask'
'''