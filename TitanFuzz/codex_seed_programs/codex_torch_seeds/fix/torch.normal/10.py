'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.normal\ntorch.normal(mean, std, size, *, out=None)\n'
import torch
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
output_data = torch.normal(mean=input_data, std=torch.ones(input_data.size()))
print('Input:', input_data)
print('Output:', output_data)