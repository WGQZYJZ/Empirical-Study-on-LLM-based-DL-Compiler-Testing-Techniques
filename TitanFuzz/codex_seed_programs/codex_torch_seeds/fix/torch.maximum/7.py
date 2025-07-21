'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.maximum\ntorch.maximum(input, other, *, out=None)\n'
import torch
data_input = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
data_other = torch.tensor([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(torch.maximum(data_input, data_other))