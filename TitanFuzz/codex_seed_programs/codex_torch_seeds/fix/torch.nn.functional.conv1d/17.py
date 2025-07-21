'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.conv1d\ntorch.nn.functional.conv1d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1)\n'
import torch
import numpy as np
input = torch.tensor(np.array([1, 2, 3, 4]).reshape(1, 1, 4), dtype=torch.float32)
weight = torch.tensor(np.array([1, 2, 3]).reshape(1, 1, 3), dtype=torch.float32)
output = torch.nn.functional.conv1d(input, weight)
print(output)