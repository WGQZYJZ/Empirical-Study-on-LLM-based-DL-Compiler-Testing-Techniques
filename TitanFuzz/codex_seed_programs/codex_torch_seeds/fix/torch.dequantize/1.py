'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dequantize\ntorch.dequantize(tensors)\n'
import torch
input_tensor = torch.randint(low=0, high=255, size=(2, 3), dtype=torch.uint8)
print('Input tensor: ', input_tensor)
output_tensor = torch.dequantize(input_tensor)
print('Output tensor: ', output_tensor)