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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, 3, padding=1, stride=2)
        super().__init__()

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.relu(v1)
        v3 = torch.sigmoid(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16)


test_inputs = [x1]
