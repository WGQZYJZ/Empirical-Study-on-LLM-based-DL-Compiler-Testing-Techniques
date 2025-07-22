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

    def forward(self, x, self_attn_layer_norm, qk, mask):
        x = self_attn_layer_norm(x)
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        q = attn_weight @ v
        return x + q



func = Model().to('cpu')

x = 1
self_attn_layer_norm = 1
qk = 1
mask = 1

test_inputs = [x, self_attn_layer_norm, qk, mask]

# JIT_FAIL
'''
direct:
'int' object is not callable

jit:
'int' object is not callable
'''