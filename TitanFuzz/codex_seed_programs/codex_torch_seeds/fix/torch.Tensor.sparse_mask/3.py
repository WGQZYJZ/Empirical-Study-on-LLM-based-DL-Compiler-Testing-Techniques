'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
import torch
x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
mask = torch.tensor([[True, False, True, False], [False, True, False, True]])
y = torch.Tensor.sparse_mask(x, mask)
print(y)