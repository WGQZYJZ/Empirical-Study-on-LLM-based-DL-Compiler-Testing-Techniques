'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.ByteTensor([[1, 0, 1], [1, 0, 0]])
output_tensor = torch.Tensor.sparse_mask(input_tensor, mask)
print('input_tensor:', input_tensor)
print('mask:', mask)
print('output_tensor:', output_tensor)