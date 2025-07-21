'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dequantize\ntorch.dequantize(tensors)\n'
import torch
import numpy as np
input_data = torch.randint(low=0, high=255, size=(1, 3, 224, 224), dtype=torch.uint8)
output_data = torch.dequantize(input_data)
print(output_data)
print(output_data.dtype)
quantized_tensor = torch.quantize_per_tensor(output_data, scale=1.0, zero_point=0, dtype=torch.quint8)
print(quantized_tensor)
print(quantized_tensor.dtype)