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

    def __init__(self, d_model, nhead, dropout_p=0.1):
        super().__init__()
        self.multihead_attn = torch.nn.MultiheadAttention(d_model, nhead, dropout_p)

    def forward(self, q, k, v, mask):
        return self.multihead_attn(q, k, v, mask)


d_model = 64
nhead = 64
func = Model(d_model, nhead, dropout_p).to('cpu')


q = torch.randn(2, 8, 64)

k = torch.randn(64, 8, 64)

v = torch.randn(64, 8, 64)
mask = 1

test_inputs = [q, k, v, mask]
