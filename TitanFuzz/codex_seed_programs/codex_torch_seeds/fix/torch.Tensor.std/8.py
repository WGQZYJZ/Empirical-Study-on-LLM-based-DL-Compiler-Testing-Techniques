'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.std\ntorch.Tensor.std(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.randn(10, 20)
std = input_tensor.std(dim=1)
print(std)