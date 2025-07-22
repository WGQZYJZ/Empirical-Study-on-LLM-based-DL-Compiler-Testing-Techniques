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
        self.vgg = torchvision.models.vgg11_bn()
        t = list(self.vgg.features.children())
        self.vgg.features = torch.nn.Sequential(*t[:16], self.vgg.features.conv3)

    def forward(self, x1):
        m1 = self.vgg(x1)
        return m1


func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]
