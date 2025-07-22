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
        self.add = torch.nn.ConvTranspose2d(1, 2, stride=3)

    def forward(self, x1):
        v1 = self.add(x1)
        v2 = torch.tanh(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(14, 1, 72, 6)


test_inputs = [x1]
