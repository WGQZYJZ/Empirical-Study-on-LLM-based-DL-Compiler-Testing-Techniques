'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor: {}'.format(input_tensor))
print('torch.Tensor.index_fill(input_tensor, 0, torch.tensor([0]), value=0.0)')
print(torch.Tensor.index_fill(input_tensor, 0, torch.tensor([0]), value=0.0))
print('torch.Tensor.index_fill(input_tensor, 1, torch.tensor([1]), value=0.0)')
print(torch.Tensor.index_fill(input_tensor, 1, torch.tensor([1]), value=0.0))