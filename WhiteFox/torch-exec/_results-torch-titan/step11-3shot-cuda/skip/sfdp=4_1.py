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

    def __init__(self, hidden_size, num_heads, attn_mask):
        super().__init__()
        self.fc = torch.nn.Linear(384, hidden_size)
        self.self_attn = torch.nn.MultiheadAttention(hidden_size, num_heads)
        self.fc_2 = torch.nn.Linear(hidden_size, 384)
        self.attn_mask = attn_mask

    def forward(self, x1):
        y1 = self.fc(x1)
        y2 = self.self_attn(y1, y1, y1, self.attn_mask)
        y3 = self.fc(y2[0])
        v1 = (x1 + y3)
        return v1




hidden_size = 128

num_heads = 1

attn_mask = torch.Tensor([[0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]).byte()

func = Model(hidden_size, n_heads, attn_mask).to('cuda')



attn_mask = torch.Tensor([[0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]).byte()



x1 = torch.randn(2, 384)


test_inputs = [attn_mask, x1]
