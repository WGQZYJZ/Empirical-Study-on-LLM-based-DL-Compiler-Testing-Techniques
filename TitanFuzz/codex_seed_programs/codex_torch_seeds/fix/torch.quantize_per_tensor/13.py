'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import numpy as np
input = torch.randn(1, 3, 224, 224)
input = input.float()
quantized_input = torch.quantize_per_tensor(input, scale=0.1, zero_point=5, dtype=torch.quint8)
print(quantized_input)
print(quantized_input.q_scale())
print(quantized_input.q_zero_point())
print(quantized_input.int_repr().numpy())
print(quantized_input.dequantize().numpy())