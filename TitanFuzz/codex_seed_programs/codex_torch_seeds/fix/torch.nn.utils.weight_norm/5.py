"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.weight_norm\ntorch.nn.utils.weight_norm(module, name='weight', dim=0)\n"
import torch
from torch.nn.utils import weight_norm
conv_layer = torch.nn.Conv2d(in_channels=3, out_channels=5, kernel_size=3, stride=1, padding=1)
conv_layer = weight_norm(conv_layer, name='weight', dim=0)
print(conv_layer)