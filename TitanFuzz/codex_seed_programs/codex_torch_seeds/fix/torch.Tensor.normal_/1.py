'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.normal_\ntorch.Tensor.normal_(_input_tensor, mean=0, std=1, *, generator=None)\n'
import torch
input_tensor = torch.randn(10, 3)
print(input_tensor)
output_tensor = torch.Tensor.normal_(input_tensor, mean=0, std=1)
print(output_tensor)