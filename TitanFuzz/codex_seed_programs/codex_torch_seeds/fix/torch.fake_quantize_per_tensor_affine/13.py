'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_tensor_affine\ntorch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)\n'
import torch
import numpy as np
input = torch.randn(3, 3).float()
quantized_tensor = torch.fake_quantize_per_tensor_affine(input, scale=0.5, zero_point=4, quant_min=0, quant_max=8)
print(quantized_tensor)