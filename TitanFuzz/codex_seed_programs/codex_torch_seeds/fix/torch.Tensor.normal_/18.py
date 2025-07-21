'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.normal_\ntorch.Tensor.normal_(_input_tensor, mean=0, std=1, *, generator=None)\n'
import torch
import torch
input_tensor = torch.ones(2, 3)
torch.Tensor.normal_(input_tensor, mean=0, std=1)
print(input_tensor)