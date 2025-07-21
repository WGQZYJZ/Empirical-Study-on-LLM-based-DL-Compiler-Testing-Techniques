'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
input_data = torch.rand(1, 1, 5, 5)
quantized_data = torch.quantize_per_tensor(input_data, scale=0.5, zero_point=3, dtype=torch.quint8)
print(quantized_data)