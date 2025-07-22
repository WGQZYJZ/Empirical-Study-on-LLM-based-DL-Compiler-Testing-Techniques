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
        pass

    def forward(self, q, k, v, mask):
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + mask
        attn_weights = torch.softmax(qk, dim=-1)
        output = attn_weights @ v
        return (output, attn_weights)


func = Model().to('cpu')


q = torch.randn(1, 1, 64, 64)

k = torch.randn(1, 1, 64, 64)

v = torch.randn(1, 1, 64, 64)

mask = torch.zeros(1, 1, 64, 64)

test_inputs = [q, k, v, mask]
