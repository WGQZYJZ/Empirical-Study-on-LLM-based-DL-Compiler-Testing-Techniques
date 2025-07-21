'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
input_data = torch.tensor([[2.0, 3.0]])
print('Input data: ', input_data)
output_data = torch.tan(input_data)
print('Output data: ', output_data)
output_data = torch.tan_(input_data)
print('Output data: ', output_data)