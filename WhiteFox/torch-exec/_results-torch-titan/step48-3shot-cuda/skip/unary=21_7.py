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
        self.deconv = torchvision.models.vgg16_bn(pretrained=True).features[40]

    def forward(self, x):
        v1 = self.deconv(x)
        v2 = torch.tanh(v1)
        return v2




func = ModelTanh().to('cuda')



x = torch.randn(1, 64, 65, 65)


test_inputs = [x]
