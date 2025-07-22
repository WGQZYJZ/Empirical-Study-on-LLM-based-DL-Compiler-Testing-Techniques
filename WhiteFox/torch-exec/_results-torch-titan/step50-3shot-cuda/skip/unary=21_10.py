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
        self.conv = torch.nn.Conv2d(3, 16, 7, stride=1, padding=3, groups=2)
        self.tanh = torch.nn.Tanh()

    def forward(self, x14):
        t1 = self.conv(x14)
        t2 = self.tanh(t1)
        return t2




func = ModelTanh().to('cuda')



x14 = torch.randn(1, 3, 49, 89)


test_inputs = [x14]
