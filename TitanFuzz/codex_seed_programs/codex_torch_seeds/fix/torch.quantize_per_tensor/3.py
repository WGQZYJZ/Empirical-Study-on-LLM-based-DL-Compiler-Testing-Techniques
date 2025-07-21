'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.quantization
input_tensor = torch.randn(3, 3)
quantized_tensor = torch.quantize_per_tensor(input_tensor, scale=1.0, zero_point=0, dtype=torch.quint8)
print('Quantized tensor: ', quantized_tensor)
print('Scale of quantized tensor: ', quantized_tensor.q_scale())