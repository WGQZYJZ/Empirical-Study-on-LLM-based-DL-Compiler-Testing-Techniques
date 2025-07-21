'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
x = torch.tensor([(- 1), 0, 1], dtype=torch.float32)
print(x)
y = torch.nn.Softsign()
print(y(x))