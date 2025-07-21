'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
input = torch.randn(1, 2, 3, dtype=torch.float32)
quantized_input = torch.quantize_per_tensor(input, scale=1.0, zero_point=0, dtype=torch.quint8)
print('Input:', input)
print('Quantized Input:', quantized_input)
'\nTask 4: Call the API torch.quantize_per_channel\ntorch.quantize_per_channel(input, scales, zero_points, axis, dtype)\n'
input = torch.randn(1, 2, 3, dtype=torch.float32)