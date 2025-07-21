'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
input_tensor = torch.quantize_per_tensor(torch.randn(3, 3), 0.1, 0, torch.quint8)
output_tensor = input_tensor.dequantize()
print(output_tensor)