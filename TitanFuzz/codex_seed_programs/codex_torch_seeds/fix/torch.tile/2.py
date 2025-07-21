'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
x = torch.FloatTensor([[1, 2], [3, 4]])
print(x)
y = torch.tile(x, (1, 2))
print(y)
y = torch.tile(x, (2, 1))
print(y)
y = torch.tile(x, (2, 2))
print(y)