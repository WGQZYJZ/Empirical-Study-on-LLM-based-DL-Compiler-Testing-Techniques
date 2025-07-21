'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_tensor_affine\ntorch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)\n'
import torch
input = torch.randn(1, 2, 3, 4)
scale = 0.5
zero_point = 1
quant_min = 0
quant_max = 2
output = torch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)
print(output)
'\nTask 4: Call the API torch.fake_quantize_per_channel_affine\ntorch.fake_quantize_per_channel_affine(input, scales, zero_points, quant_min, quant_max, axis)\n'
input = torch.randn(4, 2, 3, 4)
scales = torch.tensor([0.5, 0.5])
zero_points = torch.tensor([1, 1])