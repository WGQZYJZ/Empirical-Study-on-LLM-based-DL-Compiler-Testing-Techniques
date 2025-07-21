'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_tensor_affine\ntorch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)\n'
import torch
import torch
input_data = torch.rand(4, 4)
quantized_data = torch.fake_quantize_per_tensor_affine(input_data, scale=0.1, zero_point=5, quant_min=0, quant_max=10)
print(input_data)
print(quantized_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_channel_affine\ntorch.fake_quantize_per_channel_affine(input, scale, zero_point, axis, quant_min, quant_max)\n'
import torch
import torch
input_data = torch.rand(4, 2, 4)