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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(16, 32)
        self.linear1 = nn.Linear(32, 48)
        self.linear2 = nn.Linear(48, 16)
        self.conv = nn.Conv2d(in_channels=8, kernel_size=(3, 3), padding=0, out_channels=16, groups=1, bias=False)
        self.convtranspose = nn.ConvTranspose2d(in_channels=8, kernel_size=(3, 3), padding=0, out_channels=16, groups=1, bias=False)
        self.gru = nn.GRU(input_size=256, hidden_size=256, num_layers=2, bidirectional=True)
        self.lstm = nn.LSTM(input_size=16, hidden_size=4, num_layers=2, bidirectional=True)
        self.rnn = nn.RNN(input_size=32, hidden_size=16, num_layers=3, nonlinearity='tanh')
        self.transformer = nn.Transformer(d_model=336, nhead=16, num_encoder_layers=2, num_decoder_layers=2)

    def forward(self, x):
        x = self.layers(x)
        x = self.layers.weight
        x = self.linear1(x)
        x = torch.add(self.linear1(x), self.linear2.weight)
        x = self.conv(x)
        x = self.convtranspose(x)
        x = self.gru(x)
        x = self.lstm(x)
        x = self.rnn(x)
        x = self.transformer(x)
        x = x.mean(dim=2)
        return x




func = Model().to('cuda')



x = torch.randn(2, 8, 256, 256)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4096x256 and 16x32)

jit:
Failed running call_module L__self___layers(*(FakeTensor(..., device='cuda:0', size=(2, 8, 256, 256)),), **{}):
a and b must have same reduction dim, but got [4096, 256] X [16, 32].

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''