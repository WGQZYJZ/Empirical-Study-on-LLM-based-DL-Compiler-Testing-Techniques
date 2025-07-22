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
        self.heads = 0
        self.seq_len = 0
        self.dim = 0 // self.heads

    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.1, True)
        output = attn_weight @ value
        return output



func = Model().to('cpu')


query = torch.randn(1, 8, 8192, 2102)

key = torch.randn(1, 8, 8192, 2102)

value = torch.randn(1, 8, 8192, 2102)

attn_mask = torch.randn(1, 1, 8192, 8192)

test_inputs = [query, key, value, attn_mask]
