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
        self.conv_t = torch.nn.ConvTranspose2d()

    def forward(self):
        x1 = torch.ones([1, 1, 224, 224])
        return self.conv_t(x1)



func = Model().to('cpu')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]
