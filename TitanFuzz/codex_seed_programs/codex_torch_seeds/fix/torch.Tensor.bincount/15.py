'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bincount\ntorch.Tensor.bincount(_input_tensor, weights=None, minlength=0)\n'
import torch
input_tensor = torch.randint(0, 10, (10,))
print(input_tensor)
result = torch.Tensor.bincount(input_tensor, minlength=10)
print(result)