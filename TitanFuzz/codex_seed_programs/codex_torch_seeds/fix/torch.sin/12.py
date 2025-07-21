'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sin\ntorch.sin(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
sin_output = torch.sin(input_data)
print(sin_output)
'\nTask 4: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
cos_output = torch.cos(input_data)
print(cos_output)