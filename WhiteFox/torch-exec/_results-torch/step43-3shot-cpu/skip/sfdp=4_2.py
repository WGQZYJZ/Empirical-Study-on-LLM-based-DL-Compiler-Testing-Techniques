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

class Model(torcho.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, Q6, K6, V6, mask):
        qk = Q6 @ K6.transpose(-2, -1) / math.sqrt(Q6.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ V6
        return output



func = Model().to('cpu')


Q = torch.randn(1, 100, 32)

K = torch.randn(1, 100, 32)

V = torch.randn(1, 100, 32)


mask = (torch.rand(1, 32) > 0.7).fill_(float(-100000))

test_inputs = [Q, K, V, mask]
