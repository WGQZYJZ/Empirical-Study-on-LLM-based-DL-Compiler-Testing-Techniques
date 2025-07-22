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

class Model(nn.Module):

    def __init__(self, d_model, nhead, dropout_p):
        super().__init__()
        self.attn_module = nn.MultiheadAttention(d_model=d_model, num_heads=nhead, dropout=dropout_p)

    def forward(self, x1, x2, x3=None):
        (attention_output, attn_mask) = self.attn_module(x1, x3, x3, None)
        return (attention_output, attn_mask)


d_model = 1
nhead = 1
dropout_p = 1
func = Model(64, 8, 0.1).to('cpu')


x1 = torch.randn(1, 150, 64)

x2 = torch.randn(1, 150, 64)

x3 = torch.randn(1, 150, 64)

test_inputs = [x1, x2, x3]
