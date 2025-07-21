"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.norm\ntorch.Tensor.norm(_input_tensor, p='fro', dim=None, keepdim=False, dtype=None)\n"
import torch
input_tensor = torch.randn(4, 3, 28, 28)
norm_result = torch.Tensor.norm(input_tensor)
print(norm_result)