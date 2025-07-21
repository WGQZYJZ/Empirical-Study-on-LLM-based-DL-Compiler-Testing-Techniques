'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.real\ntorch.real(input)\n'
import torch
input_data = torch.randn(2, 2)
print('Input data:\n', input_data)
result = torch.real(input_data)
print('Result:\n', result)