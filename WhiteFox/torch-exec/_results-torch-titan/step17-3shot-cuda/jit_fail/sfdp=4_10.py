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



class MultiheadAttentionIdentity(torch.nn.MultiheadAttention):

    def forward(self, query, key, value, attn_mask=None):
        return super().forward(query, key, value, attn_mask)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.attn = MultiheadAttentionIdentity(32, 8)

    def forward(self, x1, x2):
        v1 = self.attn(x1, x2, x2)
        return v1



func = Model().to('cuda')



x1 = torch.randn(128, 32, 64)



x2 = torch.randn(128, 32, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
was expecting embedding dimension of 32, but got 64

jit:
was expecting embedding dimension of 32, but got 64
'''