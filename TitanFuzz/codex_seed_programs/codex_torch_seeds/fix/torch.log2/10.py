'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log2\ntorch.log2(input, *, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(input_data)
print(torch.log2(input_data))