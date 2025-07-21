'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eig\ntorch.Tensor.eig(_input_tensor, eigenvectors=False)\n'
import torch
_input_tensor = torch.rand(2, 2)
output_tensor = torch.Tensor.eig(_input_tensor, eigenvectors=False)
print('Input: {}'.format(_input_tensor))
print('Output: {}'.format(output_tensor))