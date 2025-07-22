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
        self.convTranspose = torch.nn.ConvTranspose2d(4, 4)

    def forward(self, x1):
        v1 = self.convTranspose(x1)
        v2 = torch.tanh(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 4, 64, 64)

test_inputs = [x1]
