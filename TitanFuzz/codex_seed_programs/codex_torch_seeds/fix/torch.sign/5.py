'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
x = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
y = torch.sign(x)
print(y)