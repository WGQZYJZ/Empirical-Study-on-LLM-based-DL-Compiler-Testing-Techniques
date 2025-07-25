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

    def __init__(self, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
        self.q_linear = Linear(d_model, d_model)
        self.k_linear = Linear(d_model, d_model)

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, mask: torch.Tensor=None):
        attn_weight = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(self.q_linear.out_features))
        if (mask is not None):
            attn_weight += mask
        attn_weight = torch.softmax(attn_weight, dim=(- 1))
        return (attn_weight @ v)



func = Model(d_model=512, num_heads=8).to('cuda')



x1 = torch.randn(1, 784, 512)



x2 = torch.randn(1, 784, 512)



x3 = torch.randn(1, 784, 512)


x3 = torch.randn(1, 784, 512)



mask = torch.zeros_like(x3.transpose(1, 2))


test_inputs = [x1, x2, x3, mask]
