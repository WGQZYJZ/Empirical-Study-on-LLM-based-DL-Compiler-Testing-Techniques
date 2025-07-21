'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.sigmoid\ntorch.nn.functional.sigmoid(input)\n'
import torch
input_data = torch.randn(2, 5)
output_data = torch.nn.functional.sigmoid(input_data)
print('Input data:', input_data)
print('Output data:', output_data)