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
        self.attn = nn.MultiheadAttention(1024, 8192)
        self.gru = nn.GRU(1024, 1024, 1, batch_first=True)

    def forward(self, x):
        (o, w) = self.attn(x, x, x, need_weights=True)
        (o, _) = self.gru(o)
        return (o, w)



func = Model().to('cpu')


x = torch.randn(1, 16, 1024)

test_inputs = [x]
