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

    def __init__(self, d_model, nhead, dim_feedforward, num_layers, dropout_p):
        super().__init__()
        self.encoder_layers = torch.nn.ModuleList([TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout_p) for i in range(num_layers)])

    def forward(self, x1, x2):
        for layer in self.encoder_layer:
            x2 = layer(x1, x2)
        return x2



d_model = 1
nhead = 1
dim_feedforward = 1
num_layers = 1
dropout_p = 1

func = Model(d_model, nhead, dim_feedforward, num_layers, dropout_p).to('cuda')



x1 = torch.randn(1, 1, 1)



x2 = torch.randn(1, 1, 1)


test_inputs = [x1, x2]
