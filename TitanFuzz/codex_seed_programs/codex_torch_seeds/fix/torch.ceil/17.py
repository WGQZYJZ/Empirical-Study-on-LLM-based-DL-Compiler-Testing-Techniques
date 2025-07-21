'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.2, 2.3, 3.4, 4.5])
torch.ceil(input_data)
print(torch.ceil(input_data))