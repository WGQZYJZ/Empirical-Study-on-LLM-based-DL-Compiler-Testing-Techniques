'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
tensor_a = torch.randn(3, 3)
tensor_b = torch.randn(3, 3)
result = torch.sub(tensor_a, tensor_b)
print(result)