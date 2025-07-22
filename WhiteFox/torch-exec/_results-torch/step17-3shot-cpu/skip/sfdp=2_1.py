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
        self.attn = MultiheadAttention()

    def forward(self, query, key, value, key_padding_mask=None, attn_mask=None):
        v = self.attn(query, key, value, key_padding_mask, attn_mask)[0]
        return v


func = Model().to('cpu')


query = torch.randn(1, 2, 3)

key = torch.randn(2, 4, 8)

value = torch.randn(2, 4, 8)

test_inputs = [query, key, value]
