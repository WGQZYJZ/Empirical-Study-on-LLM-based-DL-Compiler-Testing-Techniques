'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dequantize\ntorch.dequantize(tensors)\n'
import torch
input_data = torch.randint(low=0, high=255, size=(3, 3), dtype=torch.uint8)
print('Input data: ', input_data)
output_data = torch.dequantize(input_data)
print('Output data: ', output_data)