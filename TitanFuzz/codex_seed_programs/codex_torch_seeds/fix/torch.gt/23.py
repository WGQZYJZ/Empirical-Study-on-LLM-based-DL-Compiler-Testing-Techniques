'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gt\ntorch.gt(input, other, *, out=None)\n'
import torch
tensor_a = torch.randn(4, 4)
tensor_b = torch.randn(4, 4)
print(torch.gt(tensor_a, tensor_b))
print((tensor_a > tensor_b))