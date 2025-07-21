'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_diagonal_\ntorch.Tensor.fill_diagonal_(_input_tensor, fill_value, wrap=False)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 3))
print('Input Tensor: {}'.format(input_tensor))
torch.Tensor.fill_diagonal_(input_tensor, fill_value=1, wrap=False)
print('Output Tensor: {}'.format(input_tensor))