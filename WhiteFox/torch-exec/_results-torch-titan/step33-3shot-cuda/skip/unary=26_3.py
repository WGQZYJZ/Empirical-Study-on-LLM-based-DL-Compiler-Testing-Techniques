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
        self.conv_t = torch.nn.ConvTranspose2d(5, 46, 3, padding=1, groups=28)

    def forward(self, x):
        v1 = self.conv_t(x)
        v2 = v1.view(5, 46, 49)
        v3 = ((- 1.435) * v2)
        v4 = v2.max(dim=1)[1]
        v5 = torch.where((v2.argmax(dim=1) == v2.max(dim=1)[1].values), 1, 2)
        return v5.view(6, 85, 19)




func = Model().to('cuda')

x = 1

test_inputs = [x]
