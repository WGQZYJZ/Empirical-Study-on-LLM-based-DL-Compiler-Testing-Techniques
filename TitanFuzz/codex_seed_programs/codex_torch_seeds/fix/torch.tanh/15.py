'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tanh\ntorch.tanh(input, *, out=None)\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
print(torch.tanh(x))