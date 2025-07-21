'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
input_tensor = torch.randn(3, 4)
mask = torch.tensor([0, 0, 1], dtype=torch.bool)
output_tensor = torch.Tensor.sparse_mask(input_tensor, mask)
print('input_tensor:', input_tensor)
print('mask:', mask)
print('output_tensor:', output_tensor)