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
        self.heads = 8
        self.seq_len = 512
        self.dim = 64 // self.heads
        self.query_linear = torch.nn.Linear()
        self.qkv_linear = torch.nn.Linear()

    def forward(self, query, key, value, attn_mask):
        qk = self.qk_similarity(query, key)
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.1, True)
        output = attn_weight @ value
        return output



func = Model().to('cpu')


query = torch.randn(1, 8, 512, 64)

key = torch.randn(1, 8, 512, 64)

value = torch.randn(1, 8, 512, 64)

attn_mask = torch.randn(1, 1, 512, 512)

test_inputs = [query, key, value, attn_mask]
