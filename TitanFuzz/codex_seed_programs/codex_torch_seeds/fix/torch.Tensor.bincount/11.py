'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bincount\ntorch.Tensor.bincount(_input_tensor, weights=None, minlength=0)\n'
import torch
input_tensor = torch.tensor([[0, 1, 1, 3, 2, 1, 7]])
print(torch.Tensor.bincount(input_tensor))
print(torch.Tensor.bincount(input_tensor, minlength=8))
print(torch.Tensor.bincount(input_tensor, weights=torch.tensor([1, 1, 1, 1, 1, 1, 2])))
print(torch.Tensor.bincount(input_tensor, weights=torch.tensor([1, 1, 1, 1, 1, 1, 2]), minlength=8))