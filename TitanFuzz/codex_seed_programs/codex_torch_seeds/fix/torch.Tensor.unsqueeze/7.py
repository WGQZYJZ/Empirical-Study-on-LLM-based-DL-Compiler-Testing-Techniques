'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze\ntorch.Tensor.unsqueeze(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
output_tensor = input_tensor.unsqueeze(dim=2)
print('input_tensor: {}'.format(input_tensor))
print('output_tensor: {}'.format(output_tensor))