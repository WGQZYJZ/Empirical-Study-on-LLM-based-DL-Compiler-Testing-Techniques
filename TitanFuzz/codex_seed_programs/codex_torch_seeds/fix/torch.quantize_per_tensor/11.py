'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import torch.nn as nn
import torch.nn.quantized as nnq
import torch.quantization
X = torch.rand(3, 3).float()
X_quant = torch.quantize_per_tensor(X, scale=0.5, zero_point=5, dtype=torch.quint8)
print(X_quant)
X_dequant = X_quant.dequantize()
print(X_dequant)