'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data: ', input_data)
output_data = torch.isfinite(input_data)
print('Output data: ', output_data)