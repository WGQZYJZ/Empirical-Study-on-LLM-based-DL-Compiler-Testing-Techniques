'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fix\ntorch.fix(input, *, out=None)\n'
import torch
import torch
x = torch.tensor([(- 1.8), (- 1.2), (- 0.4), 0.4, 1.2, 1.8], dtype=torch.float32)
y = torch.fix(x)
print(y)
x = torch.tensor([(- 1.8), (- 1.2), (- 0.4), 0.4, 1.2, 1.8], dtype=torch.float32)
y = torch.fix(x, out=torch.empty_like(x))
print(y)