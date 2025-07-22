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
        self.multihead_attention = torch.nn.MultiheadAttention(17, 2)

    def forward(self, q, k, v):
        (a, _) = self.multihead_attention(q, k, v)
        return a


func = Model().to('cpu')


q = torch.randn(1, 10, 17)

k = torch.randn(1, 20, 17)

v = torch.randn(1, 20, 2)

test_inputs = [q, k, v]
