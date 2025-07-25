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
        self.conv1 = nn.Conv2d(256, 64, 3, stride=1, padding_mode='circular', padding=1)
        self.conv2 = nn.Conv2d(64, 48, 3, stride=1, padding='replicate', padding_mode='reflect')
        self.conv3 = nn.Conv2d(48, 32, 3, stride=1, padding='valid', padding_mode='zeros')
        self.conv4 = nn.Conv2d(32, 16, 3, stride=1, padding_mode='zeros')

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        v8 = (v7 * 0.5)
        v9 = (v7 * 0.7071067811865476)
        v10 = torch.erf(v9)
        v11 = (v10 + 1)
        v12 = (v8 * v11)
        v13 = self.conv3(v12)
        v14 = (v13 * 0.5)
        v15 = (v13 * 0.7071067811865476)
        v16 = torch.erf(v15)
        v17 = (v16 + 1)
        v18 = (v14 * v17)
        v19 = self.conv4(v18)
        return v19




func = Model().to('cuda')



x1 = torch.randn(1, 256, 64, 64)


test_inputs = [x1]
