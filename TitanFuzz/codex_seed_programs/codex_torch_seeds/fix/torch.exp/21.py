'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp\ntorch.exp(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 4)
print('Input data:', input_data)
exp_output = torch.exp(input_data)
print('Exponential output:', exp_output)
exp_output = torch.empty(2, 4)
torch.exp(input_data, out=exp_output)
print('Exponential output with out:', exp_output)