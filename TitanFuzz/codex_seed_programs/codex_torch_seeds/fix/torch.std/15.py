'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std\ntorch.std(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
std = torch.std(input_data)
print(std)