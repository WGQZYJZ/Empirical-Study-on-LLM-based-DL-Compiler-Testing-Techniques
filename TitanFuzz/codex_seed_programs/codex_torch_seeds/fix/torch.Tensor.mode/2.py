'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mode\ntorch.Tensor.mode(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mode = input_tensor.mode(dim=0)
print(mode)
mode = input_tensor.mode(dim=1)
print(mode)