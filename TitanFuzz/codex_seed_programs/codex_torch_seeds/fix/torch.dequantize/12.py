'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dequantize\ntorch.dequantize(tensors)\n'
import torch
input_tensor = torch.randint(0, 255, (1, 3, 8, 8), dtype=torch.uint8)
print('Input data: ', input_tensor)
output_tensor = torch.dequantize(input_tensor)
print('Output data: ', output_tensor)