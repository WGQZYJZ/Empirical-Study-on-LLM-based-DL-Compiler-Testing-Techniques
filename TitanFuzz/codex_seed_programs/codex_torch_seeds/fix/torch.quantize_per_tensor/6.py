'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import torch
X = torch.randn(3, 3)
print(X)
X_quantized = torch.quantize_per_tensor(X, 0.5, 0, torch.quint8)
print(X_quantized)
X_dequantized = X_quantized.dequantize()
print(X_dequantized)