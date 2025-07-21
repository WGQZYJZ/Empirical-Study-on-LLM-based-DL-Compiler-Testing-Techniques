'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
print('Input data: ', input_tensor)
output_tensor = torch.lgamma(input_tensor)
print('Output data: ', output_tensor)