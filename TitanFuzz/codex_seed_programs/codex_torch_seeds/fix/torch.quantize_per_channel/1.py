'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_channel\ntorch.quantize_per_channel(input, scales, zero_points, axis, dtype)\n'
import torch
input_data = torch.randn(2, 3, 4, 5, dtype=torch.float)
input_data = torch.randn(2, 3, 4, 5, dtype=torch.float)
print(input_data)
output = torch.quantize_per_channel(input_data, scales=torch.tensor([0.1, 0.2, 0.3]), zero_points=torch.tensor([3, 4, 5]), axis=1, dtype=torch.quint8)
print(output)
output = torch.quantize_per_tensor(input_data, 0.1, 3, dtype=torch.quint8)
print(output)