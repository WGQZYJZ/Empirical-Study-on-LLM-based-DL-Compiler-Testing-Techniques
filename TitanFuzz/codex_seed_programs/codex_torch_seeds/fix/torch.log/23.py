'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log\ntorch.log(input, *, out=None)\n'
import torch
x = torch.tensor([2.0, 3.0, 4.0])
y = torch.log(x)
print(y)