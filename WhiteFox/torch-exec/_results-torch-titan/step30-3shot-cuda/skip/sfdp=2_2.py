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



class PreLN(torch.nn.Module):

    def __init__(self, n_head, input_dim, output_dim, dropout_p=0.0):
        super().__init__()
        self.attention = MultiHeadAttention(n_head, input_dim)
        self.layer_norm1 = torch.nn.LayerNorm(input_dim)
        self.layer_norm2 = torch.nn.LayerNorm(input_dim)
        fc = torch.nn.Linear(input_dim, output_dim)
        if (dropout_p > 0.0):
            fc = torch.nn.Sequential(fc, torch.nn.Dropout(dropout_p))
        self.fc = torch.nn.Sequential(fc, torch.nn.GELU())

    def forward(self, x1):
        z1 = self.layer_norm1(x1)
        attention_output = self.attention(z1, z1, z1)
        z2 = self.layer_norm2((x1 + attention_output))
        output = self.fc(z2)
        return output




class Model(torch.nn.Module):

    def __init__(self, n_head, input_dim, output_dim, dropout_p=0.0):
        super().__init__()
        self.transformer = PreLN(n_head, input_dim, output_dim)

    def forward(self, x2):
        output = self.transformer(x2)
        return output




n_head = 4


input_dim = 1024


output_dim = 512

func = Model(n_head, input_dim, output_dim, dropout_p).to('cuda')



x2 = torch.randn(1, 64, 1024)


test_inputs = [x2]
