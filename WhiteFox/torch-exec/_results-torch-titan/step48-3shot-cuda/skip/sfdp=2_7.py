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

    def __init__(self, d_model, num_heads, dropout_p=0, device=torch.device('cpu')):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.head_dim = (d_model // num_heads)
        self.query = torch.nn.Linear(d_model, d_model)
        self.key = torch.nn.Linear(d_model, d_model)
        self.value = torch.nn.Linear(d_model, d_model)
        self.scaled_dot_product = ScaledDotProductAttention(dropout_p, device)

    def forward(self, x1):
        (batch_size, sequence_length, d_model) = x1.shape
        q = self.query(x1)
        k = self.key(x1)
        v = self.value(x1)
        output = self.scaled_dot_product(q, k, v)
        return output



d_model = 1
num_heads = 1
func = Model(512, 8).to('cuda')



x1 = torch.randn(1, 512, 16)


test_inputs = [x1]
