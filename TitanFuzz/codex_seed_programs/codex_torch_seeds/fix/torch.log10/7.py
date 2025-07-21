'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
input_data = torch.Tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(torch.log10(input_data))