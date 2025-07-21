'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log_normal_\ntorch.Tensor.log_normal_(_input_tensor, mean=1, std=2, *, generator=None\n'
import torch
input_tensor = torch.randn(10, 2, 3)
print(input_tensor)
torch.Tensor.log_normal_(input_tensor, mean=1, std=2)
print(input_tensor)