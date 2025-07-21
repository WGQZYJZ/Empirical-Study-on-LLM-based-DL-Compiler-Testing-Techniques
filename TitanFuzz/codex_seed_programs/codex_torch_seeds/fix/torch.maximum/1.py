'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.maximum\ntorch.maximum(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5])
other_data = torch.tensor([5, 4, 3, 2, 1])
maximum_data = torch.maximum(input_data, other_data)
print(maximum_data)