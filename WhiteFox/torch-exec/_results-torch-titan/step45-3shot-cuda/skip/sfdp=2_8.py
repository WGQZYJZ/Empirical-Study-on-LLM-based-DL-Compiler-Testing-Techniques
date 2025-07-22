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



class MultiHeadAttention(torch.nn.Module):

    def __init__(self, d_model, nheads, dropout=0.1):
        super().__init__()
        self.encoder_layer = torch.nn.TransformerEncoderLayer(d_model, nheads, dropout)

    def forward(self, x1):
        v1 = x1.permute(1, 0, 2)
        v2 = self.encoder_layer(v1)
        result = v2.permute(1, 0, 2)
        return result



d_model = 1
nheads = 1

func = MultiHeadAttention(d_model, nheads).to('cuda')



x1 = torch.randn(32, 256, 512)


test_inputs = [x1]
