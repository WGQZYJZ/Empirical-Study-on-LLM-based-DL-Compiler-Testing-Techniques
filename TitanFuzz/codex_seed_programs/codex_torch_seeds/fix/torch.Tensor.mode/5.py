'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mode\ntorch.Tensor.mode(_input_tensor, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
mode_val = input_tensor.mode(dim=1, keepdim=True)
print(mode_val)