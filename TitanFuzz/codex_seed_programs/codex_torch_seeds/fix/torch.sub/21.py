'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
other = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.float32)
result = torch.sub(input, other)
print(result)