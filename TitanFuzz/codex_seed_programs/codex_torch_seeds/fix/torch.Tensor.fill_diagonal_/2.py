'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_diagonal_\ntorch.Tensor.fill_diagonal_(_input_tensor, fill_value, wrap=False)\n'
import torch
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
print('input_tensor: ', input_tensor)
'\nTask 3: Call the API torch.Tensor.fill_diagonal_\ntorch.Tensor.fill_diagonal_(_input_tensor, fill_value, wrap=False)\n'
torch.Tensor.fill_diagonal_(input_tensor, fill_value=100, wrap=False)
print('The result of torch.Tensor.fill_diagonal_: ', input_tensor)