'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multiply\ntorch.multiply(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
other_data = torch.tensor([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(torch.multiply(input_data, other_data))