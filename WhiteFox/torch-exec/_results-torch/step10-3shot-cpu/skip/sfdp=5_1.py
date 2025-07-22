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
        self.query = torch.nn.Parameter([])
        self.key = torch.nn.Parameter([])
        self.value = torch.nn.Parameter([])

    def forward(self, x1):
        qk = self.query @ self.key.transpose(-2, -1) / math.sqrt(32)
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weights, dropout_p, True)
        output = attn_weight @ value
        return output



func = Model().to('cpu')


x1 = torch.randn(1, 32, 32)

test_inputs = [x1]
