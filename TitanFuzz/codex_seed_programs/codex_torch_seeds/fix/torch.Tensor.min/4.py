'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.min\ntorch.Tensor.min(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.min())
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.min(dim=0))
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.min(dim=0, keepdim=True))
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.min(dim=1))
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.min(dim=1, keepdim=True))