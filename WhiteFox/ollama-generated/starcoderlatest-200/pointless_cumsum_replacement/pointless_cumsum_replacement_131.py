
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.full([64, 64], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device, pin_memory=False) # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        v2 = convert_element_type(v1, x1.dtype) # Convert the elements of the tensor to the specified dtype
        v3 = torch.cumsum(v2, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v6


# Test data
import numpy as np
import torch
from nni.compression.pytorch import LevelPruner, L1FilterPruner
import os
import time
import math
import collections

import torchvision.models as models

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat((x1[:, :, 4:5], x2[:, :3, :, 4]), dim=2)
        return v

class Model_ConvOnly(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v = self.conv(x)
        return v

class Model_BatchNormOnly(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bn1 = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        v = self.bn1(x)
        return v

def prepare():
    os.environ["CUDA_VISIBLE_DEVICES"] = "0" # The code must run in the GPU mode, which you can use with CUDA 9.0 and PyTorch 1.4. Please install PyTorch on your own if needed.
    x1 = torch.randn(1, 3, 64, 64)
    x2 = torch.randn(1, 3, 64, 64)
    x_list = [x1] * 4 # list of input tensors
    x_list[0].requires_grad_(True)
    x_list[1].requires_grad_(False)

def check():
    v = torch.cat((x1[:, :, 4:5], x2[:, :3, :, 4]), dim=2)
    return v



# Main function for test
