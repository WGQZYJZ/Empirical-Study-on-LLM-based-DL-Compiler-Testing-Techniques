'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_channel\ntorch.quantize_per_channel(input, scales, zero_points, axis, dtype)\n'
import torch
import torch.quantization
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.models import resnet18
input = torch.rand(1, 3, 224, 224, dtype=torch.float)
scales = torch.tensor([0.8, 0.9, 1.0])
zero_points = torch.tensor([0, 0, 0])
axis = 1
dtype = torch.quint8
output = torch.quantize_per_channel(input, scales, zero_points, axis, dtype)
print(output)