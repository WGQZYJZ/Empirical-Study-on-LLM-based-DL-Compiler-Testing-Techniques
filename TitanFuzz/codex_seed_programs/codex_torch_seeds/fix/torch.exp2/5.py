'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp2\ntorch.exp2(input, *, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5])
print(torch.exp2(input_data))