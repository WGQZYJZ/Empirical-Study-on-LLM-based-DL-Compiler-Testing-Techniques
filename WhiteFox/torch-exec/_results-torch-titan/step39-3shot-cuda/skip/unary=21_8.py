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
        self.conv = torch.nn.ConvTranspose1d(1, 2, 4, groups=2)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        return v2




func = ModelTanh().to('cuda')



x = torch.randn(20, 1, 2)


test_inputs = [x]
