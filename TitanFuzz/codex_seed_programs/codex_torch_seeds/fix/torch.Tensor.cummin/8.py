'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
output_tensor = input_tensor.cummin(dim=1)
print(output_tensor)
print('Input Tensor: {}'.format(input_tensor))
print('Output Tensor: {}'.format(output_tensor))