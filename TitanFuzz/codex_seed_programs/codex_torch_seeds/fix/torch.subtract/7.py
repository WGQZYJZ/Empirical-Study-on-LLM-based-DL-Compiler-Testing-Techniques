'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.subtract\ntorch.subtract(input, other, *, alpha=1, out=None)\n'
import torch
tensor_a = torch.rand(3, 3)
tensor_b = torch.rand(3, 3)
tensor_c = torch.subtract(tensor_a, tensor_b)
print(tensor_c)
tensor_c = torch.subtract(tensor_a, tensor_b, alpha=2)
print(tensor_c)