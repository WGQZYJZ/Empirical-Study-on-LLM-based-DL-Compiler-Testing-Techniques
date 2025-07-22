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
        self.convBN = F.conv3d(7, 3, 3)

    def forward(self, x1):
        s = F.relu(self.convBN(x1))
        return s




func = Model().to('cuda')



x1 = torch.randn(1, 7, 4, 4, 4)


test_inputs = [x1]
