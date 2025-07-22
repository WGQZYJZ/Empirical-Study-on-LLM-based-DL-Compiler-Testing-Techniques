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

    def __init__(self, n_layer, n_head, n_embd):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        encoder_layer = Transformer.EncoderLayer(n_embd)
        self.transformer = Transformer.Encoder(encoder_layer, n_layer)
        self.n_embd = n_embd
        self.decoder = nn.Linear(768, 10)

    def forward(self, x1):
        v1 = self.transformer(x1, None)
        v2 = v1.view(-1, self.n_embd)
        return self.decoder(v2)


n_layer = 1
n_head = 1
n_embd = 1
func = Model(3, 1, 1).to('cpu')


x2 = torch.randn(10, 3, 64, 64)

test_inputs = [x2]
