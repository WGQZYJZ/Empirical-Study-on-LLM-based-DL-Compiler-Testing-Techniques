'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_quantized\ntorch.Tensor.is_quantized(_input_tensor, )\n'
import torch
input_tensor = torch.randn(4, 4)
is_quantized = torch.Tensor.is_quantized(input_tensor)
print(is_quantized)