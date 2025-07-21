'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input tensor:')
print(input_tensor)
print('\nOutput tensor:')
print(torch.Tensor.new_full(input_tensor, size=(3, 3), fill_value=0))