'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
a = torch.randn(1, 1, 3, 3)
import torch
a = torch.randn(1, 1, 3, 3)
a_quant = torch.quantize_per_tensor(a, scale=0.5, zero_point=2, dtype=torch.quint8)
print(a_quant)
'\nTask 1: Call the API torch.quantize_per_channel\ntorch.quantize_per_channel(input, scales, zero_points, axis, dtype)\n'