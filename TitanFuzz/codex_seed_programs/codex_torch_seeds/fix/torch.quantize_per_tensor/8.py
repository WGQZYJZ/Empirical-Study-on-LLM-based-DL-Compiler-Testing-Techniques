'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import torch
input_data = torch.randn(1, 3, 224, 224, dtype=torch.float32)
quantized_input = torch.quantize_per_tensor(input_data, scale=0.3, zero_point=2, dtype=torch.quint8)
print('Input data:', input_data)
print('Quantized input:', quantized_input)
dequantized_input = quantized_input.dequantize()
print('Dequantized input:', dequantized_input)
quantized_input = torch.quantize_per_tensor(input_data, scale=0.3, zero_point=2, dtype=torch.qint8)
print('Quantized input:', quantized_input)
dequantized_input = quantized_input.dequantize()
print('Dequantized input:', dequantized_input)