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
        self.upsample = torch.nn.functional.interpolate(scale_factor=2)
        self.conv = torch.nn.ConvTranspose2d(3, 128, kernel_size=3, padding=1, stride=1)

    def forward(self, x1):
        v1 = self.upsample(x1)
        v2 = self.conv(v1)
        v3 = torch.relu(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]
