'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sin\ntorch.sin(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(torch.sin(input_data))
'\nTask 4: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
print(torch.cos(input_data))