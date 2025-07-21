'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_and\ntorch.bitwise_and(input, other, *, out=None)\n'
import torch
x = torch.tensor([[True, False], [False, False]], dtype=torch.bool)
y = torch.tensor([[True, False], [True, False]], dtype=torch.bool)
torch.bitwise_and(x, y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_or\ntorch.bitwise_or(input, other, *, out=None)\n'
import torch
x = torch.tensor([[True, False], [False, False]], dtype=torch.bool)
y = torch.tensor([[True, False], [True, False]], dtype=torch.bool)