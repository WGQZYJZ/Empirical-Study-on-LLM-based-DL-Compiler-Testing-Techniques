'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_tensor_affine\ntorch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)\n'
import torch
print(torch.__version__)
input_data = torch.arange(0, 10, dtype=torch.float)
print('input_data: ', input_data)
scale = 1
zero_point = 0
quant_min = 0
quant_max = 10
quantized_tensor = torch.fake_quantize_per_tensor_affine(input_data, scale, zero_point, quant_min, quant_max)
print('quantized_tensor: ', quantized_tensor)
quantization_error = (quantized_tensor - input_data)
print('quantization_error: ', quantization_error)