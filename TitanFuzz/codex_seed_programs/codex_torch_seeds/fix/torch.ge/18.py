'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ge\ntorch.ge(input, other, *, out=None)\n'
import torch
import torch
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
print(x)
y = torch.ge(x, 2)
print(y)