"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.norm\ntorch.Tensor.norm(_input_tensor, p='fro', dim=None, keepdim=False, dtype=None)\n"
import torch
input_tensor = torch.arange(0, 9).view(3, 3)
print(input_tensor)
norm_result = input_tensor.norm()
print(norm_result)
norm_result = input_tensor.norm(p=2)
print(norm_result)
norm_result = input_tensor.norm(dim=1)
print(norm_result)
norm_result = input_tensor.norm(p=1, dim=1)
print(norm_result)
norm_result = input_tensor.norm(p=2, dim=1, keepdim=True)
print(norm_result)