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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(196, 287, 2, input_padding=(1, 1), padding=(1, 1), dilation=1, groups=1, bias=True, padding_mode='zeros')

    def forward(self, x):
        t1 = self.conv(x)
        t2 = torch.tanh(t1)
        return t2



func = ModelTanh().to('cpu')


x = torch.randn(1, 196, 32)

test_inputs = [x]
