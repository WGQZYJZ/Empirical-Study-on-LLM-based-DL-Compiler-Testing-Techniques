'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
input_tensor = torch.randn(3, 3)
mask = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
sparse_masked_tensor = torch.Tensor.sparse_mask(input_tensor, mask)
print('Input tensor = {}'.format(input_tensor))
print('Mask = {}'.format(mask))
print('Sparse masked tensor = {}'.format(sparse_masked_tensor))