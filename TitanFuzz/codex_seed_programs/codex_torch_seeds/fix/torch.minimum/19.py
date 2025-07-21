'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.minimum\ntorch.minimum(input, other, *, out=None)\n'
import torch
input_data = torch.randn(4, 4, requires_grad=True)
other_data = torch.randn(4, 4, requires_grad=True)
output_data = torch.minimum(input_data, other_data)
print('Output data: ', output_data)