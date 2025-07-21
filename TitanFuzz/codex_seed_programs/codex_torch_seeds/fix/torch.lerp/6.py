'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=torch.float32)
y = torch.tensor([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], dtype=torch.float32)
out = torch.lerp(x, y, 0.5)
print(out)