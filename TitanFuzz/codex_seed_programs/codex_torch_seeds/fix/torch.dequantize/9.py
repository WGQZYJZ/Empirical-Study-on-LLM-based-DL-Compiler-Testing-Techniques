'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dequantize\ntorch.dequantize(tensors)\n'
import torch
import torch.quantization
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.uint8)
print('Input tensor: ', input_tensor)
print('Task 3: Call the API torch.dequantize')
output_tensor = torch.dequantize(input_tensor)
print('Output tensor: ', output_tensor)