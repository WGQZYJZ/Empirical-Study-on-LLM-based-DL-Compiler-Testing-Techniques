'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter\ntorch.Tensor.masked_scatter(_input_tensor, mask, tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
mask = torch.tensor([[1, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0]])
tensor = torch.tensor([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
torch.Tensor.masked_scatter(input_tensor, mask, tensor)