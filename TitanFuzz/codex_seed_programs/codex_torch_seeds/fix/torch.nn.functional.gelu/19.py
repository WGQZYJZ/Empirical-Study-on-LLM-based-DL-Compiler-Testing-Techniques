'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gelu\ntorch.nn.functional.gelu(input)\n'
import torch
x = torch.tensor([(- 1.5), 0, 1.5])
y = torch.nn.functional.gelu(x)
print(y)