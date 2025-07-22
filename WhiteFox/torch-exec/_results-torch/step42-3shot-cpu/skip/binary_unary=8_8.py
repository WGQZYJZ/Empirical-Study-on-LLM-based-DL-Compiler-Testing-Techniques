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
        self.vgg16 = torchvision.models.vgg16()
        self.vgg16.classifier[6] = torch.nn.Linear(25088, 1024)
        self.vgg16.classifier[7] = torch.nn.ReLU()
        self.vgg16.classifier[8] = torch.nn.Dropout()
        self.l3 = torch.nn.Linear(1024, 1024)

    def forward(self, x):
        v1 = self.vgg16(x)
        v2 = self.l3(v1)
        v3 = torch.relu(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]
