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

class AttentionMechanism(torch.nn.Module):

    def __init__(self, num_heads):
        super().__init__()

    def qk(self, query, key, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        return qk

    def attn_weight(self, query, key, attn_mask):
        qk = self.qk(query, key, attn_mask)
        attn_weight = torch.softmax(qk, dim=-1)
        return attn_weight

    def attn(self, attn_weight, value):
        attn_out = attn_weight @ value
        return attn_out


num_heads = 1
func = AttentionMechanism(8).to('cpu')


x2 = torch.randn(2, 16, 100)

x3 = torch.randn(2, 16, 100)

x4 = torch.randn(2, 1, 100, 100)

test_inputs = [x2, x3, x4]

# JIT_FAIL
'''
direct:
Module [AttentionMechanism] is missing the required "forward" function

jit:
Module [AttentionMechanism] is missing the required "forward" function
'''