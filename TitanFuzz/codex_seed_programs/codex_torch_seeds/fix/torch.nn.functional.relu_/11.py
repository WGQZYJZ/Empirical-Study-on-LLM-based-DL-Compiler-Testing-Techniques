'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
import torch
x = torch.tensor([(- 1.0), 1.0, 2.0])
y = torch.nn.functional.relu_(x)
print(y)