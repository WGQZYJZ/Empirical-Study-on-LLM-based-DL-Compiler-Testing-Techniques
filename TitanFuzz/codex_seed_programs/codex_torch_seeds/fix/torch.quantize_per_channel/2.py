'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_channel\ntorch.quantize_per_channel(input, scales, zero_points, axis, dtype)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
input = torch.randn(3, 3, 3, 3)
quantized_input = torch.quantize_per_channel(input, scales=torch.tensor([1.0, 1.0, 1.0]), zero_points=torch.tensor([0, 0, 0]), axis=0, dtype=torch.quint8)
print('input: ', input)
print('quantized_input: ', quantized_input)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch