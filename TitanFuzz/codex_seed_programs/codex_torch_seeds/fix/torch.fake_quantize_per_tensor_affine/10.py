'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_tensor_affine\ntorch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)\n'
import torch
import torch
input = torch.randn(3, 3)
output = torch.fake_quantize_per_tensor_affine(input, scale=1.0, zero_point=0, quant_min=0, quant_max=255)
print(output)