'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
tanh = torch.nn.Tanh()
output = tanh(input_data)
print('Output: ', output)
output = torch.tanh(input_data)
print('Output: ', output)