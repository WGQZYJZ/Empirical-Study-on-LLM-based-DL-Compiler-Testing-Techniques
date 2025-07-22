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
        self.attn = torch.nn.MultiheadAttention(query, key, num_heads, dropout=0.0, bias=True, add_bias_kv=True, add_zero_attn=True)

    def forward(self, x1, x2):
        (v1, v2) = self.attn(x1, x2, x2)
        return (v1, v2)



func = Model().to('cuda')



x1 = torch.randn(1, 64, 64)



x2 = torch.randn(1, 128, 64)


test_inputs = [x1, x2]
