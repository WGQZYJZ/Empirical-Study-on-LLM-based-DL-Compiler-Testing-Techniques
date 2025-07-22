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
        self.layer1 = ((nn.Linear(2, 2) + 1) * 2)
        self.layer2 = (nn.Conv2d(1, 1, 3, groups=1) - 1)
        self.layer3 = nn.Sigmoid()
        self.layer4 = nn.LayerNorm([1, 2, 3])
        self.layer5 = ((nn.LayerNorm([1, 2, 3]) * nn.Sigmoid()) - (nn.Conv2d(1, 1, 3) + 2))

    def forward(self, x):
        x = self.layer1
        x = self.layer2
        x = self.layer3(self.layer4[self.layer5](x))
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]
