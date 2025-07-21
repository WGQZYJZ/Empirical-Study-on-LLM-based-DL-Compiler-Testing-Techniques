'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rot90\ntorch.Tensor.rot90(_input_tensor, k, dims)\n'
import torch
print('\nTask 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
input_tensor = torch.randn(3, 4, 5)
print('input_tensor = ', input_tensor)
print('input_tensor.size() = ', input_tensor.size())
print('\nTask 3: Call the API torch.Tensor.rot90')
print('torch.Tensor.rot90(input_tensor, k=1, dims=(1, 2)) = ', torch.Tensor.rot90(input_tensor, k=1, dims=(1, 2)))
print('torch.Tensor.rot90(input_tensor, k=2, dims=(1, 2)) = ', torch.Tensor.rot90(input_tensor, k=2, dims=(1, 2)))