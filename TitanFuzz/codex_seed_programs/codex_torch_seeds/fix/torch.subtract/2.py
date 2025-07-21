'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.subtract\ntorch.subtract(input, other, *, alpha=1, out=None)\n'
import torch
input_data = torch.Tensor([1, 2, 3, 4, 5])
other_data = torch.Tensor([2, 2, 2, 2, 2])
result = torch.subtract(input_data, other_data)
print(result)