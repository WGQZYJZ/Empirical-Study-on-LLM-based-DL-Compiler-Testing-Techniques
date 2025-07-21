'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
input_data = torch.randn(1, 2)
print('Input data: ', input_data)
tanh_output = torch.nn.Tanh()
print('Tanh output: ', tanh_output(input_data))