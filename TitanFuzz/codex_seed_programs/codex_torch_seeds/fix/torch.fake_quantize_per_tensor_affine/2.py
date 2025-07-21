'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_tensor_affine\ntorch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)\n'
import torch
import numpy as np
'\nimport PyTorch\n'
'\nGenerate input data\n'
input_data = torch.rand(1, 3, 224, 224, dtype=torch.float32)
'\nCall the API torch.fake_quantize_per_tensor_affine\ntorch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)\n'
output = torch.fake_quantize_per_tensor_affine(input_data, 1.0, 0, 0, 255)
print('input_data:', input_data)
print('output:', output)