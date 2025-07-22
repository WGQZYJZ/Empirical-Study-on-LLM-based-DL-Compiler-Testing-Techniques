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

    def __init__(self, *, d_model=256, nhead=8, dropout=0.2):
        super(Model, self).__init__()
        self.multihead_attention = nn.MultiheadAttention(d_model=d_model, num_heads=nhead, dropout=dropout)

    def forward(self, x1, x2):
        (y1, y2) = self.multihead_attention(x1, x1, x2)
        return (y1, y2)



func = Model().to('cuda')



x1 = torch.randn(2, 6, 15)



x2 = torch.randn(2, 14, 15)


test_inputs = [x1, x2]
