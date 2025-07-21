'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
input_data = torch.randn(2, 3)
tanh_output = torch.nn.Tanh()(input_data)
print('Input data: ', input_data)
print('Output of Tanh: ', tanh_output)