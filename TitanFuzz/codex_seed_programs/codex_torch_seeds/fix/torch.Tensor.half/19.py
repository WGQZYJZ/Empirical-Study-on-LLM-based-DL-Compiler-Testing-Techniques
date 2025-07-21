'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.half\ntorch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
input_tensor = torch.randn(3, 3).float()
print('input_tensor:', input_tensor)
output_tensor = input_tensor.half()
print('output_tensor:', output_tensor)