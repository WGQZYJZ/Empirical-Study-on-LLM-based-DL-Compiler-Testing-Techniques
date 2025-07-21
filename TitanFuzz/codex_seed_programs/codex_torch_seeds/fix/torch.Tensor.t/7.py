'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.t())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, 0, 1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.transpose(0, 1))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unbind\ntorch.Tensor.unbind(_input_tensor, dim=0)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.unbind(dim=0))