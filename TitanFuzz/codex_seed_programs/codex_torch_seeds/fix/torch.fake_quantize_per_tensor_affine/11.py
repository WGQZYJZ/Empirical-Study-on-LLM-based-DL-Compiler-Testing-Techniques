'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_tensor_affine\ntorch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)\n'
import torch
import torch
input = torch.rand(3, 4)
torch.fake_quantize_per_tensor_affine(input, scale=0.5, zero_point=2, quant_min=0, quant_max=5)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_channel_affine\ntorch.fake_quantize_per_channel_affine(input, scales, zero_points, quant_min, quant_max, axis)\n'
import torch
import torch
input = torch.rand(3, 4)