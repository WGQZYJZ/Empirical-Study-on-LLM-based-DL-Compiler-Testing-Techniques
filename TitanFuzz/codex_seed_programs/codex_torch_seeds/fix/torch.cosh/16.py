'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cosh\ntorch.cosh(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
print(torch.cosh(input_data))