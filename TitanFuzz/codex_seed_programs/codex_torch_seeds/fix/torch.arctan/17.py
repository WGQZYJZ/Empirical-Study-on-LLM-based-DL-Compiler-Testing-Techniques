'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1.0), 0.0, 1.0])
y = torch.arctan(x)
print('The arctan of input tensor x:', x)
print('is:', y)