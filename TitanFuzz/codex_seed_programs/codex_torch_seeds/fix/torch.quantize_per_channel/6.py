'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_channel\ntorch.quantize_per_channel(input, scales, zero_points, axis, dtype)\n'
import torch
import torch
input = torch.randn(2, 3, 4, 5)
output = torch.quantize_per_channel(input, scales=torch.tensor([1.0, 2.0, 3.0]), zero_points=torch.tensor([0, 0, 0]), axis=1, dtype=torch.quint8)
print(output)
print(output.q_per_channel_scales())
print(output.q_per_channel_zero_points())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import torch