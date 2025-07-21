'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool3d\ntorch.nn.MaxPool3d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = torch.randn(1, 1, 4, 4, 4)
maxpool_layer = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(1, 1, 1), padding=(0, 0, 0))
output_data = maxpool_layer(input_data)
print(output_data.shape)