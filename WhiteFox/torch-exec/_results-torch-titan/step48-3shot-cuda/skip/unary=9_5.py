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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.add = torch.add
        self.clip = torch.nn.functional.clamp
        self.div = torch.div

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = self.add(t1, 3)
        t3 = self.clip(t2, min=0, max=6)
        t4 = self.div(t3, 6)
        return t4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]
