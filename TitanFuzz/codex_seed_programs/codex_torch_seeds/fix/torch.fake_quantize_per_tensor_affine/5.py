'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_tensor_affine\ntorch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)\n'
import torch
import numpy as np
input_data = torch.randn(3, 3)
scale = 1.0
zero_point = 0
quant_min = 0
quant_max = 255
quantized_data = torch.fake_quantize_per_tensor_affine(input_data, scale, zero_point, quant_min, quant_max)
print('input_data: {}'.format(input_data))
print('quantized_data: {}'.format(quantized_data))