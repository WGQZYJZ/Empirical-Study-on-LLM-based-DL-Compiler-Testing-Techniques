'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu_\ntorch.nn.functional.elu_(input, alpha=1.)\n'
import torch
x = torch.tensor([(- 1), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float32)
y = torch.nn.functional.elu_(x, alpha=1.0)
print('x:', x)
print('y:', y)