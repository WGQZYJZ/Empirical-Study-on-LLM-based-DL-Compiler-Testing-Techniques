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

    def __init__(self, input_size=256, hidden_size=512, num_layers=2, dropout_p=0.1):
        super().__init__()
        self.decoder = torch.nn.Linear(input_size, hidden_size)
        self.decoder_layers = torch.nn.ModuleList([torch.nn.GRUCell(hidden_size, hidden_size)] * (num_layers - 1))
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, X1, X2):
        d = self.decoder(X1)
        for cell in self.decoder_layers:
            d = self.dropout(d)
            d = gelu(cell(d, X2))
        d = self.dropout(d)
        d = self.decoder(d)
        d = self.decoder(d)
        return d



func = Model().to('cpu')


X1 = torch.randn(1, 256)

X2 = torch.randn(1, 256)

test_inputs = [X1, X2]

# JIT_FAIL
'''
direct:
name 'gelu' is not defined

jit:
NameError: name 'gelu' is not defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''